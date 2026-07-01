from datetime import UTC, datetime
from uuid import UUID, uuid4

from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, HttpUrl
from webhooks import send_webhooks

router = APIRouter()


class ShortLinkCreate(BaseModel):
    target_url: HttpUrl


class ShortLink(BaseModel):
    id: UUID
    short_code: str
    target_url: HttpUrl
    clicks: int = 0


links: dict[str, ShortLink] = {}

# Issue logic related to links, also payload and webhooks at one place - system grows then coupling as repeat - something happened -> Event bus or management system
@router.post("/links")
def create_short_link(data: ShortLinkCreate) -> ShortLink:
    short_code = uuid4().hex[:6]

    link = ShortLink(
        id=uuid4(),
        short_code=short_code,
        target_url=data.target_url,
    )

    links[short_code] = link

    payload = {
        "type": "link.created",
        "link_id": str(link.id),
        "short_code": link.short_code,
        "target_url": str(link.target_url),
    }

    send_webhooks(payload) # Post request to webhook when shortlink created

    return link


@router.get("/links")
def list_short_links() -> list[ShortLink]:
    return list(links.values())


@router.get("/{short_code}")
def redirect_to_target(short_code: str) -> RedirectResponse:
    link = links.get(short_code)

    if link is None:
        raise HTTPException(status_code=404, detail="Short link not found")

    link.clicks += 1

    payload = {
        "type": "link.clicked",
        "link_id": str(link.id),
        "short_code": link.short_code, # provide short url
        "target_url": str(link.target_url), # target long url
        "clicks": link.clicks,
        "clicked_at": datetime.now(UTC).isoformat(),
    }

    send_webhooks(payload) # click request to webhook when clicked

    return RedirectResponse(str(link.target_url))
