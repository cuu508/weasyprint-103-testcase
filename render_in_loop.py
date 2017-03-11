import os
from weasyprint import HTML

BASE_DIR = os.path.dirname(__file__)

soup = """
<!DOCTYPE html>
<html>
<body>
<style>

@page {
    @bottom-center {
        background: url("footer.svg") no-repeat center center;
        content: "";
    }

    @bottom-left {
        content: "lorem ipsum";
        font-family: "MontserratLight", "Times New Roman";

    }
}

@font-face {
    font-family: MontserratLight;
    src: url("Montserrat-Light.otf") format("opentype");
}

</style>
</body>
</html>
"""


for i in range(0, 1000):
    print("Iteration %d" % i)
    html = HTML(string=soup, base_url=BASE_DIR)
    html.write_pdf()
