from abc import ABC, abstractmethod
from dataclasses import asdict, astuple, dataclass, field

# ================================================================
# USER DATACLASS WITH ALL FEATURES FROM THE VIDEO
# ================================================================


# Frozen dataclass: makes the instance immutable (prevents attribute reassignment); blocks assignments to fields after initialization
# Order dataclass: adds comparison methods (__lt__, __le__, __gt__, __ge__) based on field definitions
# Slots dataclass: uses __slots__ to reduce memory usage and remove instance dictionary. Not add attributes dynamically.
# kw_only dataclass: makes all fields keyword-only in the constructor (no positional arguments allowed)
@dataclass(order=True, slots=True, kw_only=True, frozen=True)
class User:
    name: str
    email: str
    tags: list[str] = field(default_factory=list[str]) # default field, still mutable even if frozen=True (shallow immutability);  field(repr=False) to exclude from repr
    slug: str = field(init=False) # derived field (not in constructor) and computed later in __post_init__, created once per user

    def __post_init__(self): # method called after object creation
        # Normalize name and create slug
        normalized_name = self.name.strip().title()
        slugified = normalized_name.lower().replace(" ", "-") # alternate, self.slug = slugified if frozen=False

        object.__setattr__(self, "name", normalized_name) # since frozen=True, we use
        object.__setattr__(self, "slug", slugified)  # since frozen=True, we use

    @property # A property in Python is a way to define methods that behave like attributes. It lets you add logic (validation, computation) when getting, setting, or deleting an attribute while keeping the clean obj.attribute syntax
    def domain(self) -> str: # Getter - when run User.domain
        """Return the domain part of the email address."""
        return self.email.split("@")[-1]

    def contact_card(self) -> str:
        """Return a formatted contact card."""
        return f"{self.name} <{self.email}>"

    @classmethod # Class method: method bound to the class and not the instance; first parameter is cls (the class itself), generate user object from email
    def from_email(cls, email: str) -> "User": # -> Self
        """Create a User from only an email address."""
        local = email.split("@")[0].replace(".", " ")
        name = local.title()
        return cls(name=name, email=email)


# ================================================================
# ABSTRACT DATACLASS EXAMPLE - Define shared interface for different account types
# ================================================================


@dataclass
class Account(ABC):
    owner: str
    base_fee: float

    @property
    @abstractmethod
    def monthly_fee(self) -> float: 
        ...


@dataclass
class FreeAccount(Account):
    @property
    def monthly_fee(self) -> float:
        return 0.0


@dataclass
class PremiumAccount(Account):
    extra_storage_gb: int = 100

    @property
    def monthly_fee(self) -> float:
        return self.base_fee + (self.extra_storage_gb * 0.10)


# ================================================================
# MAIN WITH RUNNING EXAMPLES
# ================================================================


def main():
    print("\n=== Creating Users ===")
    u1 = User(name="alice", email="alice@example.com")
    u2 = User(name="bob", email="bob@example.com")
    print("u1:", u1)
    print("u2:", u2)

    print("\n=== Using from_email constructor ===")
    u3 = User.from_email("john.doe@company.com")
    print("u3:", u3)

    print("\n=== Comparing Users (order=True) ===")
    print("u1 < u2:", u1 < u2)
    print("Sorted:", sorted([u2, u1, u3]))

    print("\n=== Frozen Dataclass Behavior ===") # this works for changing mutable fields even if frozen=True ex. lists
    try:
        u1.name = "Charlie"  # should fail
    except Exception as e:
        print("Attempting to reassign u1.name:", e)

    

    print("\n=== Shallow Immutability Example ===")
    u1.tags.append("allow")  # works because tags is a list (mutable), frozen=True only prevents reassignment of the field itself
    u1.tags.append("admin")
    print("u1.tags after append:", u1.tags)
    # Dataclass built in ways for serialization to convert to dict or tuple
    print("\n=== Serialization ===")
    print("asdict(u1):", asdict(u1))
    print("astuple(u1):", astuple(u1))

    print("\n=== Account Types (Abstract Dataclasses) ===")
    free = FreeAccount(owner="Alice", base_fee=0)
    premium = PremiumAccount(owner="Bob", base_fee=5) # can specify extra_storage_gb if desired
    print("FreeAccount monthly fee:", free.monthly_fee) 
    print("PremiumAccount monthly fee:", premium.monthly_fee)


if __name__ == "__main__":
    main()