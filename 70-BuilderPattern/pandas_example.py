import pandas as pd

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
styled = (
    df.style.set_caption("Styled DataFrame") # Builder for style as define step by step and finally build
    .highlight_max(axis=0)
    .format("{:.2f}")
    .background_gradient(cmap="viridis")
)

print(styled.to_html())