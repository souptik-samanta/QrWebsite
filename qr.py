import qrcode
import base64
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Souptik's World</title>
<style>
body {
  margin: 0;
  font-family: 'Roboto', sans-serif;
  background: linear-gradient(to right, #1f4037, #99f2c8);
  color: #fff;
}
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 50px;
  background: rgba(0, 0, 0, 0.6);
}
header .logo {
  font-size: 24px;
  font-weight: bold;
  text-transform: uppercase;
}
header nav a {
  margin: 0 15px;
  text-decoration: none;
  color: #fff;
  font-size: 16px;
}
.hero {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
}
.hero h1 {
  font-size: 36px;
}
.section {
  padding: 60px 20px;
  text-align: center;
}
.footer {
  background: rgba(0, 0, 0, 0.6);
  padding: 10px;
  text-align: center;
}
</style>
</head>
<body>
<header>
  <div class="logo">Souptik's World</div>
  <nav>
    <a href="#about">About</a>
    <a href="#projects">Projects</a>
    <a href="#contact">Contact</a>
  </nav>
</header>
<div class="hero">
  <h1>Welcome to Souptik's World</h1>
  <p>Exploring Tech, Gaming, and Creativity!</p>
</div>
<section id="about" class="section">
  <h2>About Me</h2>
  <p>I'm Souptik, a tech enthusiast passionate about coding and innovation.</p>
</section>
<section id="projects" class="section">
  <h2>Projects</h2>
  <p>Check out my creations on <a href="https://github.com/souptik-samanta" target="_blank">GitHub</a>.</p>
</section>
<section id="contact" class="section">
  <h2>Contact</h2>
  <p>Email: <a href="mailto:souptiksamanta20141188@gmail.com">souptiksamanta20141188@gmail.com</a></p>
</section>
<footer class="footer">
  <p>Life's a soup, and I'm a fork. Glory to HCP</p>
</footer>
</body>
</html>"""
encoded_html = base64.b64encode(html_content.encode('utf-8')).decode('utf-8')
data_url = f"data:text/html;base64,{encoded_html}"
qr = qrcode.QRCode(
    version=40,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=6,
    border=4,
)
qr.add_data(data_url)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("img_name.png")
