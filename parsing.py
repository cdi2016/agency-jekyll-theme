from bs4 import BeautifulSoup
html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<title>
		Document
	</title>
	<link href="http://trada.vnsecurity.net/" rel="canonical">
	<!-- Social: Twitter -->
	<title>
		Trà Đá Hacking
	</title>
	<link href="/img/favicons/favicon.ico" rel="shortcut icon">
	<link href="/img/favicons/apple-touch-icon-152x152.png" rel="apple-touch-icon" sizes="152x152">
	<link href="/img/favicons/apple-touch-icon-144x144.png" rel="apple-touch-icon" sizes="144x144">
	<link href="/img/favicons/apple-touch-icon-120x120.png" rel="apple-touch-icon" sizes="120x120">
	<link href="/img/favicons/apple-touch-icon-114x114.png" rel="apple-touch-icon" sizes="114x114">
	<link href="/img/favicons/apple-touch-icon-76x76.png" rel="apple-touch-icon" sizes="76x76">
	<link href="/img/favicons/apple-touch-icon-72x72.png" rel="apple-touch-icon" sizes="72x72">
	<link href="/img/favicons/apple-touch-icon-60x60.png" rel="apple-touch-icon" sizes="60x60">
	<link href="/img/favicons/apple-touch-icon-57x57.png" rel="apple-touch-icon" sizes="57x57">
	<link href="/img/favicons/favicon-196x196.png" rel="icon" type="image/png">
	<link href="/img/favicons/favicon-160x160.png" rel="icon" type="image/png">
	<link href="/img/favicons/favicon-96x96.png" rel="icon" type="image/png">
	<link href="/img/favicons/favicon-32x32.png" rel="icon" type="image/png">
	<link href="/img/favicons/favicon-16x16.png" rel="icon" type="image/png">
	<link href="/css/main.css" rel="stylesheet">
</link>
</link>
</link>
</link>
</link>
</link>
</link>
</link>
</link>
</link>
</link>
</link>
</link>
</link>
</link>
</link>
</head>
<body>
	<section class="partners" id="partners">
		<div class="content-wrapper">
			<div class="col-lg-10 col-lg-offset-1">
				<h3>
					Ban tổ chức
				</h3>
				<h5>
					Đơn vị tổ chức chính
				</h5>
				<ul class="list-inline">
					<li>
						<a href="http://www.vnsecurity.net" target="_blank">
							<img alt="VNSecurity" src="/img/organizers/vnsec.png" title="nhóm nghiên cứu chuyên sâu về bảo mật máy tính lâu đời nhất tại Việt Nam">
						</img>
					</a>
				</li>
			</ul>
		</div>
	</div>
</section>
</body>
</html>
<h3>
	Nhà tài trợ
</h3>
<h5>
	Tài trợ kinh phí
</h5>
<ul class="list-inline">
	<li>
		<a href="mailto:trada@vnsecurity.net?Subject=Sponsor" target="_blank">
			<img alt="Sponsor " src="/img/partners/sponsor1.png" title="Please contact if you want to sponsor">
		</img>
	</a>
</li>
<li>
	<a href="mailto:trada@vnsecurity.net?Subject=Sponsor" target="_blank">
		<img alt="Sponsor " src="/img/partners/sponsor1.png" title="Please contact if you want to sponsor">
	</img>
</a>
</li>
</ul>
<h5>
	Hỗ trợ truyền thông và tài trợ khác
</h5>
<ul class="list-inline">
	<li style="width: 120px;">
		<a href="#" target="_blank">
			<img alt="INCO Startup Center" src="/img/partners/inco.png" title="INCO Startup Center - Hỗ trợ truyền thông">
		</img>
	</a>
</li>
<li style="width: 120px;">
	<a href="#" target="_blank">
		<img alt="UNESCO-CEP" src="/img/partners/unesco-cep.png" title="Trung Tâm UNESCO Văn hóa Giáo dục và Đào tạo - Hỗ trợ truyền thông">
	</img>
</a>
</li>
</ul>
<a class="btn btn-primary waves-effect waves-button waves-light waves-float" href="mailto:trada@vnsecurity.net?Subject=Sponsor">
	Trở thành nhà tài trợ
</a>


"""
soup = BeautifulSoup(html_doc, 'html.parser')

with open("abc.html", 'w') as f:
	f.write(soup.prettify())
