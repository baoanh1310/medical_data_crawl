import json
from bs4 import BeautifulSoup as soup

text = '''
<div class="pulic-price-drug">
<div class=""> </div><div class=""> <div class="bg-white"> <div class="detail-content"> <div>
<div class="layout-content"> <div class="mt-20" id="list-medicine10"> <div class="box-filter"> <div class="list-medicine mt-10" id="list-medicine10"> <div class="box-filter"> <div class="filter-left"> <div class="box-search"> <a href="javascript:;" class="form-control search-advanced"><span class="pr-5">Tìm kiếm nâng cao</span><span style="float:right;"><i class="fas fa-angle-down"></i></span></a> </div> <div class="box-search box-search-input"> <input type="text" name="filters[suggestTitle]" class="form-control" value="" onchange="VHV.App.modules[10].filters.suggestTitle = $(this).val();VHV.App.modules[10].reload();" class="form-control" placeholder="Tìm kiếm theo tên thuốc"> <button class="btn btn-default"><i class="fas fa-search"></i></button> </div> <div class="text-center space search-ok"> <button class="btn btn-success btnSearch">Tìm kiếm</button> </div> </div> <div class="filter-right pull-right"> <div class="inline-block" style="vertical-align: middle;"> <select class="form-control" onchange="VHV.App.modules[10].orderBy = this.value;VHV.App.modules[10].reload();"> <option value="">Sắp xếp theo</option> <option value="price DESC" >Giá cao nhất</option>
<option value="price ASC" >Giá thấp nhất</option>
<option value="sortTitle ASC" >Tên A - Z</option>
<option value="sortTitle DESC" >Tên Z - A</option>
</select> </div> </div> </div> </div> </div> <div class="clearfix"></div> <div class="row content-search-advanced mt-10" >
<div class="col-md-3 col-sm-12 col-lg-3 col-xs-12 " >
<div class="form-group  " > <label  >Số GPLH/GPNK</label>
<input class="form-control" type="text" name="filters[numberLicense]" value="" onchange="VHV.App.modules[10].filters.numberLicense = $(this).val();VHV.App.modules[10].reload();" placeholder="Nhập Số GPLH/GPNK"> </div></div><div class="col-md-3 col-sm-12 col-lg-3 col-xs-12 " >
<div class="form-group  " > <label  >Đơn vị kê khai</label>
<input class="form-control" type="text" name="filters[manufacture]" value="" onchange="VHV.App.modules[10].filters.manufacture = $(this).val();VHV.App.modules[10].reload();" placeholder="Nhập đơn vị kê khai"> </div></div><div class="col-md-6 col-sm-12 col-lg-6 col-xs-12 " >
<div class="form-group  " > <label  >Giá</label>
<div class="row d-flex" style="align-items: center">
<div class="col-md-5    price-from" >
<input type="hidden" id="input19442" value="" class="vhv-form-number"  class="form-control from" onchange="var currentModule = VHV.App.modules[10], input=this, value = this.value;VHV.App.modules[10].filters.priceFrom = this.value.trim();VHV.App.modules[10].reload();" placeholder="Nhập giá"/><input
type="text" value="" size="16" id="numberInput19442" title="" class="formNumberInput form-control from "
placeholder="Nhập giá"/> </div><div class="col-md-1    " >
<span >đến</span> </div><div class="col-md-5    " >
<input type="hidden" id="input19443" value="" class="vhv-form-number"  class="form-control price" onchange="var currentModule = VHV.App.modules[10], input=this, value = this.value;VHV.App.modules[10].filters.priceTo = this.value.trim();VHV.App.modules[10].reload();" placeholder="Nhập giá"/><input
type="text" value="" size="16" id="numberInput19443" title="" class="formNumberInput form-control price "
placeholder="Nhập giá"/> </div><div class="col-md-1    price-vnd" >
<div>VNĐ</div> </div></div></div></div><div class="col-md-12 col-sm-12  col-xs-12 text-center search-in" >
<button class="btn btn-default btnSearch">Tìm kiếm</button> </div></div></div></div><style> .content-search-advanced{ display: none; }
@media(min-width:769px){ .prices{ margin-bottom:20px; }
.filter-left .space{ margin-right:10px; }
.search-in{ display:none; }
}
@media(max-width:768px) { .prices { margin-bottom: 20px; }
.filter-left .space{ margin-bottom:10px; }
.list-medicine .box-filter .filter-left .box-search { margin-bottom: 10px; margin-right: 0px; }
.search-ok{ display:none; }
}
@media(max-width:425px) { .price-from{ margin-bottom:10px; }
.price-vnd{ margin-top:10px; }
}
.popver-infor .text-center a{ font-size: 16px; color: #0077c5; }
.box-filter .filter-left{ display: inline-flex; }
.box-filter .filter-left .box-search { margin-right: 10px; position: relative; }
.box-filter .filter-left .box-search .btn-default { position: absolute; top: 0; left: 0; background: none; border: 0; color: var(--brand-primary); }
.box-search-input .form-control{ padding-left: 35px; }
.box-search .form-control { border: 1px solid #ccd6dd; }
.box-filter i { color: var(--brand-primary); }
.list-medical-table .table>thead>tr{ background: #226c9d; }
.list-medical-table { margin-top: 20px; }
.list-medical-table .table>thead>tr>th { color: #FFF; border-right: 1px solid #fff; }
.list-medical-table .table>tbody>tr>td { border-right: 1px dashed #ccc !important; vertical-align: middle; }
.title-img { display: inline-flex; }
.tb-img .img{ width: 55px; height: 55px; object-fit: cover; border-radius: 50%; }
.tb-title { padding-top: 10px; font-weight: 600; margin-left: 10px; }
.tb-title a { text-decoration: none; }
.tb-price { color: #2ca01c; font-weight: 600; }
.list-medical-table .table>tbody>td { font-size: 16px; }
</style> </div> <div class="layout-content wrapper-table"> <div class="row mt-20 m-0">
<div class="layout-detail col-md-12 p-0">
<div class="table-responsive">
<table class="table table-data table-striped">
<thead>
<tr>
<th scope="col" style="width:30px;">Ngày kê khai</th>
<th scope="col" class="table-1">Tên thuốc</th>
<th scope="col" class="table-1">Tên HC</th>
<th scope="col" class="table-1">NĐ/HL</th>
<th scope="col" class="table-1">Số GPLH/GPNK</th>
<th scope="col" class="table-1">Quy cách đóng gói</th>
<th scope="col" class="table-1">ĐVT</th>
<th scope="col" class="table-1">Cơ sở SX</th>
<th scope="col" class="table-1">Nước SX</th>
<th scope="col" class="table-1">Đơn vị KK</th>
<th scope="col" class="table-1">Giá</th>
</tr>
</thead>
<tbody>
 
<tr data-id="5fbf74c655dd6d49db0af7b0">
<td>18/04/2018</td>
<td>
<div class="name-product row m-0" >
<div class="img-product mr-10 col-lg-2 col-md-3 col-sm-4 p-0 col-xs-3 hidden"><img class="img-small" src=/App/images/no-image-news.png width="50px" height="50px"alt="" title="">
<div class="img-product-detail">
<div><img src=/App/images/no-image-news.png width="auto" height="auto" alt="" title=""></div>
<div class="title-product-a" >
<a href="javascript: void(0);" data-x-modal="Project.MedicalPrice.Home.MedicalPrice.Drug.detail" data-service="Project.MedicalPrice.Home.Product.Drug.select" data-popup="1" data-x-popup="backdrop:'static',keyboard: false," data-modal-class="modal-lg popup-thgv" data-grid-module-parent-id="10" title="Chi tiết">Xem chi tiết<i class="fas fa-arrow-right pl-10"></i></a>
</div>
</div>
</div>
<div class="mr-10 title-product col-lg-10 col-md-9 col-sm-8 col-xs-9">
<a href="https://congkhaiyte.moh.gov.vn/?page=Project.MedicalPrice.Home.MedicalPrice.Drug.detail&productId=5fbf74c655dd6d49db0af7b0">Olan 5</a>
</div>
</div>
</td>
<td>Olanzapin 5mg - 5mg</td>
<td>NULL</td>
<td>VN-20287-17</td>
<td>Hộp 3 vỉ x 10 Viên</td>
<td>Viên</td>
<td></td>
<td></td>
<td>Cty CP DP TW Codupha</td>
<td class="tb-price text-right">1.200</td>
</tr>
 
<tr data-id="5fbf74c655dd6d49db0af7a2">
<td>17/11/2020</td>
<td>
<div class="name-product row m-0" >
<div class="img-product mr-10 col-lg-2 col-md-3 col-sm-4 p-0 col-xs-3 hidden"><img class="img-small" src=/App/images/no-image-news.png width="50px" height="50px"alt="" title="">
<div class="img-product-detail">
<div><img src=/App/images/no-image-news.png width="auto" height="auto" alt="" title=""></div>
<div class="title-product-a" >
<a href="javascript: void(0);" data-x-modal="Project.MedicalPrice.Home.MedicalPrice.Drug.detail" data-service="Project.MedicalPrice.Home.Product.Drug.select" data-popup="1" data-x-popup="backdrop:'static',keyboard: false," data-modal-class="modal-lg popup-thgv" data-grid-module-parent-id="10" title="Chi tiết">Xem chi tiết<i class="fas fa-arrow-right pl-10"></i></a>
</div>
</div>
</div>
<div class="mr-10 title-product col-lg-10 col-md-9 col-sm-8 col-xs-9">
<a href="https://congkhaiyte.moh.gov.vn/?page=Project.MedicalPrice.Home.MedicalPrice.Drug.detail&productId=5fbf74c655dd6d49db0af7a2">Dloe 4</a>
</div>
</div>
</td>
<td>Ondansetron (dưới dạng Ondansetron hydrochloride dihydrate) 4mg/2ml</td>
<td>4mg/2ml</td>
<td>VN-16669-13</td>
<td>Hộp 5 vỉ x 5 ống 2ml</td>
<td>Ống</td>
<td></td>
<td></td>
<td>Công ty cổ phần dược trung ương 3</td>
<td class="tb-price text-right">30.000</td>
</tr>
 
<tr data-id="5fbf74c655dd6d49db0af79c">
<td>25/09/2020</td>
<td>
<div class="name-product row m-0" >
<div class="img-product mr-10 col-lg-2 col-md-3 col-sm-4 p-0 col-xs-3 hidden"><img class="img-small" src=/App/images/no-image-news.png width="50px" height="50px"alt="" title="">
<div class="img-product-detail">
<div><img src=/App/images/no-image-news.png width="auto" height="auto" alt="" title=""></div>
<div class="title-product-a" >
<a href="javascript: void(0);" data-x-modal="Project.MedicalPrice.Home.MedicalPrice.Drug.detail" data-service="Project.MedicalPrice.Home.Product.Drug.select" data-popup="1" data-x-popup="backdrop:'static',keyboard: false," data-modal-class="modal-lg popup-thgv" data-grid-module-parent-id="10" title="Chi tiết">Xem chi tiết<i class="fas fa-arrow-right pl-10"></i></a>
</div>
</div>
</div>
<div class="mr-10 title-product col-lg-10 col-md-9 col-sm-8 col-xs-9">
<a href="https://congkhaiyte.moh.gov.vn/?page=Project.MedicalPrice.Home.MedicalPrice.Drug.detail&productId=5fbf74c655dd6d49db0af79c">Bru-cod</a>
</div>
</div>
</td>
<td>Cefpodoxim (dưới dạng Cefpodoxim proxetil)  50mg/5ml</td>
<td>50mg/5ml</td>
<td>VN-16641-13</td>
<td>Hộp 1 lọ</td>
<td>Lọ</td>
<td></td>
<td></td>
<td>Công ty cổ phần xuất nhập khẩu y tế Việt Nam</td>
<td class="tb-price text-right">25.100</td>
</tr>
 
<tr data-id="5fbf74c655dd6d49db0af7a6">
<td>29/11/2019</td>
<td>
<div class="name-product row m-0" >
<div class="img-product mr-10 col-lg-2 col-md-3 col-sm-4 p-0 col-xs-3 hidden"><img class="img-small" src=/App/images/no-image-news.png width="50px" height="50px"alt="" title="">
<div class="img-product-detail">
<div><img src=/App/images/no-image-news.png width="auto" height="auto" alt="" title=""></div>
<div class="title-product-a" >
<a href="javascript: void(0);" data-x-modal="Project.MedicalPrice.Home.MedicalPrice.Drug.detail" data-service="Project.MedicalPrice.Home.Product.Drug.select" data-popup="1" data-x-popup="backdrop:'static',keyboard: false," data-modal-class="modal-lg popup-thgv" data-grid-module-parent-id="10" title="Chi tiết">Xem chi tiết<i class="fas fa-arrow-right pl-10"></i></a>
</div>
</div>
</div>
<div class="mr-10 title-product col-lg-10 col-md-9 col-sm-8 col-xs-9">
<a href="https://congkhaiyte.moh.gov.vn/?page=Project.MedicalPrice.Home.MedicalPrice.Drug.detail&productId=5fbf74c655dd6d49db0af7a6">Briozcal</a>
</div>
</div>
</td>
<td>Calci (dưới dạng Calci carbonat 1,25g) 500mg; Vitamin D3 125IU</td>
<td>500mg, 125IU</td>
<td>VN-22339-19</td>
<td>Hôp 3 vỉ x 10 viên</td>
<td>Viên</td>
<td></td>
<td></td>
<td>Công ty Cổ Phần Xuất Nhập Khẩu Y tế Tp. Hồ Chí Minh</td>
<td class="tb-price text-right">3.759</td>
</tr>
 
<tr data-id="5fbf74c655dd6d49db0af7a0">
<td>17/11/2020</td>
<td>
<div class="name-product row m-0" >
<div class="img-product mr-10 col-lg-2 col-md-3 col-sm-4 p-0 col-xs-3 hidden"><img class="img-small" src=/App/images/no-image-news.png width="50px" height="50px"alt="" title="">
<div class="img-product-detail">
<div><img src=/App/images/no-image-news.png width="auto" height="auto" alt="" title=""></div>
<div class="title-product-a" >
<a href="javascript: void(0);" data-x-modal="Project.MedicalPrice.Home.MedicalPrice.Drug.detail" data-service="Project.MedicalPrice.Home.Product.Drug.select" data-popup="1" data-x-popup="backdrop:'static',keyboard: false," data-modal-class="modal-lg popup-thgv" data-grid-module-parent-id="10" title="Chi tiết">Xem chi tiết<i class="fas fa-arrow-right pl-10"></i></a>
</div>
</div>
</div>
<div class="mr-10 title-product col-lg-10 col-md-9 col-sm-8 col-xs-9">
<a href="https://congkhaiyte.moh.gov.vn/?page=Project.MedicalPrice.Home.MedicalPrice.Drug.detail&productId=5fbf74c655dd6d49db0af7a0">Budesonide Teva 0,5mg/2ml</a>
</div>
</div>
</td>
<td>Budesonide</td>
<td>0,5mg/2ml</td>
<td>VN-15282-12</td>
<td>Hộp 30 ống 2ml</td>
<td>Ống</td>
<td></td>
<td></td>
<td>CÔNG TY TNHH DKSH PHARMA VIỆT NAM</td>
<td class="tb-price text-right">12.950</td>
</tr>
 
<tr data-id="5fbf74c655dd6d49db0af7a4">
<td>31/08/2020</td>
<td>
<div class="name-product row m-0" >
<div class="img-product mr-10 col-lg-2 col-md-3 col-sm-4 p-0 col-xs-3 hidden"><img class="img-small" src=/App/images/no-image-news.png width="50px" height="50px"alt="" title="">
<div class="img-product-detail">
<div><img src=/App/images/no-image-news.png width="auto" height="auto" alt="" title=""></div>
<div class="title-product-a" >
<a href="javascript: void(0);" data-x-modal="Project.MedicalPrice.Home.MedicalPrice.Drug.detail" data-service="Project.MedicalPrice.Home.Product.Drug.select" data-popup="1" data-x-popup="backdrop:'static',keyboard: false," data-modal-class="modal-lg popup-thgv" data-grid-module-parent-id="10" title="Chi tiết">Xem chi tiết<i class="fas fa-arrow-right pl-10"></i></a>
</div>
</div>
</div>
<div class="mr-10 title-product col-lg-10 col-md-9 col-sm-8 col-xs-9">
<a href="https://congkhaiyte.moh.gov.vn/?page=Project.MedicalPrice.Home.MedicalPrice.Drug.detail&productId=5fbf74c655dd6d49db0af7a4">Torfin-50</a>
</div>
</div>
</td>
<td>Sildenafil (dưới dạng Sildenafil citrat) 50mg</td>
<td>50 mg</td>
<td>VN-17231-13</td>
<td>Hộp 1 vỉ x 4 viên</td>
<td>Viên</td>
<td></td>
<td></td>
<td>Công ty TNHH Nutri-Pharma USA</td>
<td class="tb-price text-right">6.000</td>
</tr>
 
<tr data-id="5fbf74c655dd6d49db0af79e">
<td>05/11/2020</td>
<td>
<div class="name-product row m-0" >
<div class="img-product mr-10 col-lg-2 col-md-3 col-sm-4 p-0 col-xs-3 hidden"><img class="img-small" src=/App/images/no-image-news.png width="50px" height="50px"alt="" title="">
<div class="img-product-detail">
<div><img src=/App/images/no-image-news.png width="auto" height="auto" alt="" title=""></div>
<div class="title-product-a" >
<a href="javascript: void(0);" data-x-modal="Project.MedicalPrice.Home.MedicalPrice.Drug.detail" data-service="Project.MedicalPrice.Home.Product.Drug.select" data-popup="1" data-x-popup="backdrop:'static',keyboard: false," data-modal-class="modal-lg popup-thgv" data-grid-module-parent-id="10" title="Chi tiết">Xem chi tiết<i class="fas fa-arrow-right pl-10"></i></a>
</div>
</div>
</div>
<div class="mr-10 title-product col-lg-10 col-md-9 col-sm-8 col-xs-9">
<a href="https://congkhaiyte.moh.gov.vn/?page=Project.MedicalPrice.Home.MedicalPrice.Drug.detail&productId=5fbf74c655dd6d49db0af79e">Axcel Loratadine  Tablet</a>
</div>
</div>
</td>
<td>loratadine</td>
<td>10mg</td>
<td>VN-21048-18</td>
<td>Hộp 10 vỉ x 10 viên</td>
<td>Viên</td>
<td></td>
<td></td>
<td>Công ty cổ phần XNK Y tế Tp HCM YTECO</td>
<td class="tb-price text-right">1.800</td>
</tr>
 
<tr data-id="5fbf74c555dd6d49db0af78c">
<td>22/10/2020</td>
<td>
<div class="name-product row m-0" >
<div class="img-product mr-10 col-lg-2 col-md-3 col-sm-4 p-0 col-xs-3 hidden"><img class="img-small" src=/App/images/no-image-news.png width="50px" height="50px"alt="" title="">
<div class="img-product-detail">
<div><img src=/App/images/no-image-news.png width="auto" height="auto" alt="" title=""></div>
<div class="title-product-a" >
<a href="javascript: void(0);" data-x-modal="Project.MedicalPrice.Home.MedicalPrice.Drug.detail" data-service="Project.MedicalPrice.Home.Product.Drug.select" data-popup="1" data-x-popup="backdrop:'static',keyboard: false," data-modal-class="modal-lg popup-thgv" data-grid-module-parent-id="10" title="Chi tiết">Xem chi tiết<i class="fas fa-arrow-right pl-10"></i></a>
</div>
</div>
</div>
<div class="mr-10 title-product col-lg-10 col-md-9 col-sm-8 col-xs-9">
<a href="https://congkhaiyte.moh.gov.vn/?page=Project.MedicalPrice.Home.MedicalPrice.Drug.detail&productId=5fbf74c555dd6d49db0af78c">Piperacillin/ Tazobactam Kabi 4g/0,5g</a>
</div>
</div>
</td>
<td>Piperacilin, Tazobactam</td>
<td>4g Piperacillin; 0,5g Tazobactam</td>
<td>VN-13544-11</td>
<td>Hộp 1 lọ, hộp 10 lọ</td>
<td>Lọ</td>
<td></td>
<td></td>
<td>Công ty cổ phần Fresenius Kabi Việt Nam</td>
<td class="tb-price text-right">105.000</td>
</tr>
 
<tr data-id="5fbf74c555dd6d49db0af796">
<td>05/10/2020</td>
<td>
<div class="name-product row m-0" >
<div class="img-product mr-10 col-lg-2 col-md-3 col-sm-4 p-0 col-xs-3 hidden"><img class="img-small" src=/App/images/no-image-news.png width="50px" height="50px"alt="" title="">
<div class="img-product-detail">
<div><img src=/App/images/no-image-news.png width="auto" height="auto" alt="" title=""></div>
<div class="title-product-a" >
<a href="javascript: void(0);" data-x-modal="Project.MedicalPrice.Home.MedicalPrice.Drug.detail" data-service="Project.MedicalPrice.Home.Product.Drug.select" data-popup="1" data-x-popup="backdrop:'static',keyboard: false," data-modal-class="modal-lg popup-thgv" data-grid-module-parent-id="10" title="Chi tiết">Xem chi tiết<i class="fas fa-arrow-right pl-10"></i></a>
</div>
</div>
</div>
<div class="mr-10 title-product col-lg-10 col-md-9 col-sm-8 col-xs-9">
<a href="https://congkhaiyte.moh.gov.vn/?page=Project.MedicalPrice.Home.MedicalPrice.Drug.detail&productId=5fbf74c555dd6d49db0af796">CKDCipol-N 25mg (Đóng gói và xuất xưởng bởi: Chong Kun Dang Pharmaceutical Corp., đ/c: 797-48 Manghyang-ro, Seonggeo-eup, Seobuk-gu, Choenan-si, Chungcheongnam-do, Repubic of Korea)</a>
</div>
</div>
</td>
<td>Cyclosporin 25mg</td>
<td>NULL</td>
<td>VN-18193-14</td>
<td>Hộp 10 vỉ x 5 viên</td>
<td>Viên</td>
<td></td>
<td></td>
<td>Công ty TNHH Bình Việt Đức</td>
<td class="tb-price text-right">13.000</td>
</tr>
 
<tr data-id="5fbf74c555dd6d49db0af78e">
<td>08/11/2018</td>
<td>
<div class="name-product row m-0" >
<div class="img-product mr-10 col-lg-2 col-md-3 col-sm-4 p-0 col-xs-3 hidden"><img class="img-small" src=/App/images/no-image-news.png width="50px" height="50px"alt="" title="">
<div class="img-product-detail">
<div><img src=/App/images/no-image-news.png width="auto" height="auto" alt="" title=""></div>
<div class="title-product-a" >
<a href="javascript: void(0);" data-x-modal="Project.MedicalPrice.Home.MedicalPrice.Drug.detail" data-service="Project.MedicalPrice.Home.Product.Drug.select" data-popup="1" data-x-popup="backdrop:'static',keyboard: false," data-modal-class="modal-lg popup-thgv" data-grid-module-parent-id="10" title="Chi tiết">Xem chi tiết<i class="fas fa-arrow-right pl-10"></i></a>
</div>
</div>
</div>
<div class="mr-10 title-product col-lg-10 col-md-9 col-sm-8 col-xs-9">
<a href="https://congkhaiyte.moh.gov.vn/?page=Project.MedicalPrice.Home.MedicalPrice.Drug.detail&productId=5fbf74c555dd6d49db0af78e">Apotel max 10mg/ml Solution for Infusion</a>
</div>
</div>
</td>
<td>Paracetamol 1000mg/100ml - 1000mg/100ml</td>
<td>1000mg/100ml</td>
<td>VN-21528-18</td>
<td>Hộp 1, 10, 20, 50 gói</td>
<td>Gói</td>
<td></td>
<td></td>
<td>CÔNG TY CỔ PHẦN DƯỢC PHẨM TENAMYD</td>
<td class="tb-price text-right">45.000</td>
</tr>
 
</tbody>
</table>
</div>
</div>
</div>
<style>
.table-1 {
width: 250px;
}
.table-5 {
width: 300px;
}
.text-total-item{
font-size: 20px;
font-weight: 700;
margin-bottom: 20px;
}
.highcharts-container{
width: auto !important;
text-align: center !important;
}
</style>
 </div> </div> </div>  <div class="mt-10 pagination-wrapper mb-10"> Tổng số bản ghi: 62.438 <div class="text-right">
<div id="pagination10" class="default-pagination btn-group"></div></div><div class="form-inline ">
<div class="options-itemsPerPage btn-group dropup"> <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"> 10 <i class="caret"></i> </button> <ul class="dropdown-menu" style="width: auto; min-width: 60px;"> <li><a data-value="20" href="javascript:void(0);" onclick="VHV.App.modules[10].itemsPerPage = 20;VHV.App.modules[10].reload();">20 / trang</a></li> <li><a data-value="50" href="javascript:void(0);" onclick="VHV.App.modules[10].itemsPerPage = 50;VHV.App.modules[10].reload();">50 / trang</a></li> <li><a data-value="100" href="javascript:void(0);" onclick="VHV.App.modules[10].itemsPerPage = 100;VHV.App.modules[10].reload();">100 / trang</a></li> <li><a data-value="200" href="javascript:void(0);" onclick="VHV.App.modules[10].itemsPerPage = 200;VHV.App.modules[10].reload();">200 / trang</a></li> <li><a data-value="500" href="javascript:void(0);" onclick="VHV.App.modules[10].itemsPerPage = 500;VHV.App.modules[10].reload();">500 / trang</a></li> </ul> </div> <div class="options-page btn-group pl-10 hidden"><span class="pr-10" style="display: inline-block; vertical-align: middle">Đến</span><input type="hidden" id="input19444" value="" class="vhv-form-number"  style="width: 60px;" class="form-control" onchange="var currentModule = VHV.App.modules[10], input=this, value = this.value;VHV.App.modules[10].pageNo = this.value; VHV.App.modules[10].reload();"/><input
type="text" value="" size="16" id="numberInput19444" title="" class="formNumberInput form-control "
style="width: 60px;"/> </div></div><style> .form-inline .dropup .dropdown-menu{ left: auto; right:0; }
</style></div> </div></div><style> .toggle-filter10{ padding-left: 5px; padding-right: 5px; }
@media (min-width: 768px) { .toggle-filter10{ display: none; }
}
#module10 .form-action-right>button{ border-bottom-left-radius: 0; border-top-left-radius: 0; min-width: 108px; }
@media (max-width: 767px) { .toggle-filter10,#module10 .form-action-left .hasCheckAllActionShow,#module10 .form-action-left .btn-check-all{ border-right: none !important; }
#module10 .form-action-left.active{ background-color: #fff; padding: 10px; z-index: 22; flex: 0 0 100%; -webkit-flex: 0 0 100%; border: 1px solid #eaeaea; border-radius: 4px; position: absolute; top: 100%; left: 0; }
#module10 .form-action-right>button{ min-width: unset; }
#module10 .form-action-left.active>div:not(.hasCheckAllActionShow), #module10 .form-action-left.active .btn-check-all, #module10 .form-action-left.active .hasCheckAllActionShow{ margin-bottom: 10px; }
#module10 .form-action-left:not(.active)>div:not(.hasCheckAllActionShow){ display: none; }
#module10 .default-pagination .prev,#module10 .default-pagination .next{ display: none; }
#module10 .default-pagination .prev+a{ display: none; }
#module10 .default-pagination{ display: flex; display: -webkit-flex; }
#module10 .default-pagination a,#module10 .default-pagination span{ padding: 3px 5px; border: 1px solid #eaeaea; margin: 0 1px; min-width: 27px; border-radius: 0; }
#module10 .default-pagination .current{ border: none; }
#module10 .options-itemsPerPage .dropdown-menu{ left: auto; right: 0; }
}
#module10 .form-action-left-wrapper{ padding: 5px; border-radius: 4px; background-color: #ffffff; border: 1px solid #e7ebf8; height: 34px; white-space: nowrap; position: relative; }
@media (min-width: 768px) { #module10 .form-action-left .smartselect > button > .ss-label { max-width: 250px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; display: block; }
#module10 .form-action-left .smartselect > button { padding-right: 25px; }
#module10 .form-action-left .select2-container--default .select2-selection--single .select2-selection__arrow { right: 5px; }
#module10 .form-action-left .ss-caret, #module10 .form-action-left .select2-container--default .select2-selection--single .select2-selection__arrow b { font-family: "Font Awesome 5 Free", sans-serif; font-weight: 600; -moz-osx-font-smoothing: grayscale; -webkit-font-smoothing: antialiased; display: inline-block; font-style: normal; font-variant: normal; text-rendering: auto; line-height: 1; border: none; margin: 0; width: 10px; height: 10px; right: 5px; top: 8px; }
#module10 .form-action-left .btn { background-color: transparent !important; }
#module10 .form-action-left .select2-container--default .select2-selection--single .select2-selection__rendered { line-height: 22px; }
#module10 .form-action-left .select2-container--default .select2-selection--single .select2-selection__arrow b { margin-top: -5px; }
#module10 .form-action-left .ss-caret:before, #module10 .form-action-left .select2-container--default .select2-selection--single .select2-selection__arrow b:before { content: "\f107"; }
#module10 .smartselect > select { display: none; }
#module10 .form-action-left .select2-container, #module10 .form-action-left .select2-container--default .select2-selection--single, #module10 .form-action-left .form-control { border: none; border-radius: 0; height: 100%; padding-top: 0; padding-bottom: 0; box-shadow: none; }
#module10 .form-action-left label { margin-bottom: 0; }
#module10 .form-action-left > *:not(:last-child) { border-right: 1px solid #e7ebf8; }
#module10 .form-action-left > div .select2-selection__rendered, #module10 .form-action-left .select2-container--default .select2-selection--single .select2-selection__arrow { border: none; border-radius: 0; height: 100%; line-height: normal; }
}
#module10 .form-action-right>.form-control{ border-color: #e7ebf8; }
#module10 .form-action-right{ flex: 1; -webkit-flex: 1; }
#module10 .form-action-right>.form-control{ border-bottom-right-radius: 0; border-top-right-radius: 0; }
#module10 .f-display{ display: -webkit-flex; display: flex; }
.item-actions .action{ padding-left: 5px; padding-right: 5px; border-right: 1px solid #ccc; }
.item-actions .action:first-child{ padding-left: 0; }
.item-actions .action:last-child{ border-right: none; }
.group-input-inline>label{ font-weight: normal; }
.pagination-wrapper{ text-align: right; }
.pagination-wrapper > div{ display: inline-block; }
.pagination-wrapper > div:not(:first-of-type){ margin-left: 10px; }
@media(min-width: 1200px){ .table-tt-giaodky .group-input-inline label{ min-width: 120px; }
}
@media screen and (max-width: 1199px) { .mobile-fixWidth > div, .mobile-fixWidth > .table { width: 250%; max-width: 250%; }
}
@media (max-width: 767px){ #region-help-button{ display: contents; }
#form10{ position: relative; /*float: right;*/
}
#form10 .form-action{ position: absolute; top:-40px; height: 0; padding: 0; }
#form10 .form-action .form-action-left-wrapper{ padding: 0; border: unset; }
#form10 .form-action .form-action-left-wrapper .form-action-left.active{ left: unset; /*right: 0;*/
}
}
@media (max-width: 425px){ #form10 .form-action .form-action-left-wrapper .form-action-left.active{ width: calc(100vw - 70px); }
}
.cms-ant{ background: transparent; }
.form-action textarea.form-control{ min-height: 60px; }
</style><script type="text/javascript">;
</script>
<script type="text/javascript" id="script19442">VHV.load('3rdparty/jQuery/autoNumeric-1.7.4.js', function(){ $('#numberInput19442').autoNumeric({ aSep: '.', aDec: ',', mDec: '2', aSign: '', vMax: '10000000000000', vMin: '-1000000000000', pSign: 'p', aPad: false }).keypress(function(event){
if ( event.which == 13 ) { $('#input19442').val($('#numberInput19442').autoNumericGet()); }
}).change(function(){
var value = $('#numberInput19442').val(); if(value == ''){ $('#input19442').val('').change();
$('#numberInput19442').attr('value',''); }else{
$('#input19442').val($('#numberInput19442').autoNumericGet()).change();
$('#numberInput19442').attr('value',$('#numberInput19442').val()).autoNumericSet($('#input19442').val()); }
});
if($('#input19442').val()) { $('#numberInput19442').autoNumericSet($('#input19442').val()); }
});
</script>
<script type="text/javascript">
;
</script>
<script type="text/javascript" id="script19443">VHV.load('3rdparty/jQuery/autoNumeric-1.7.4.js', function(){ $('#numberInput19443').autoNumeric({ aSep: '.', aDec: ',', mDec: '2', aSign: '', vMax: '10000000000000', vMin: '-1000000000000', pSign: 'p', aPad: false }).keypress(function(event){
if ( event.which == 13 ) { $('#input19443').val($('#numberInput19443').autoNumericGet()); }
}).change(function(){
var value = $('#numberInput19443').val(); if(value == ''){ $('#input19443').val('').change();
$('#numberInput19443').attr('value',''); }else{
$('#input19443').val($('#numberInput19443').autoNumericGet()).change();
$('#numberInput19443').attr('value',$('#numberInput19443').val()).autoNumericSet($('#input19443').val()); }
});
if($('#input19443').val()) { $('#numberInput19443').autoNumericSet($('#input19443').val()); }
});
</script>
<script type="text/javascript">
;
$('.search-advanced').click(function(){ $('.content-search-advanced').slideToggle(); $('.search-advanced .fas').toggleClass('fa-angle-down fa-angle-up'); });
;
VHV.using ($.extend(
$.parseJSON(decode64('eyJsYXlvdXQiOiJQcm9qZWN0Lk1lZGljYWxQcmljZS5Ib21lLk1lZGljYWxQcmljZS5EcnVnLmxpc3QiLCJpdGVtc1BlclBhZ2UiOjEwLCJ0b3RhbEl0ZW1zIjo2MjQzOCwicGFnZU5vIjoyLCJzZXJ2aWNlIjoiUHJvamVjdC5NZWRpY2FsUHJpY2UuSG9tZS5NZWRpY2FsUHJpY2UuRHJ1Zy5zZWxlY3RBbGwiLCJ3aWRnZXRDb2RlIjoiTXVsdGltZWRpYSIsInR5cGUiOiJNZWRpY2FsUHJpY2UuRHJ1ZyIsInBhdGgiOiJDb250ZW50In0=')),{"module":"Content.Listing","page":"Project.MedicalPrice.Home.MedicalPrice.Drug.list","id":"10","modulePosition":"0","moduleParentId":"-1"}),{
totalItems: 62438,
filters: [],
dontGoTop: true,
pageNo: 2,
itemsPerPage: 10 
});
$('#assetAssign10').loadModule('Content.Listing',{
layout:"Software.AssetManagement.Asset.Allocation.listAllocation",
service: "Software.AssetManagement.AssetRelation.Allocation.selectAll",
"filters[assetId]": "",
orderBy: "createdTime DESC",
itemsPerPage: 10
});
$(document).ready(function(){
$('[data-toggle="popover"]').popover();
});
;
</script>
<script type="text/javascript" id="script19444">VHV.load('3rdparty/jQuery/autoNumeric-1.7.4.js', function(){ $('#numberInput19444').autoNumeric({ aSep: '.', aDec: ',', mDec: '2', aSign: '', vMax: '10000000000000', vMin: '-1000000000000', pSign: 'p', aPad: false }).keypress(function(event){
if ( event.which == 13 ) { $('#input19444').val($('#numberInput19444').autoNumericGet()); }
}).change(function(){
var value = $('#numberInput19444').val(); if(value == ''){ $('#input19444').val('').change();
$('#numberInput19444').attr('value',''); }else{
$('#input19444').val($('#numberInput19444').autoNumericGet()).change();
$('#numberInput19444').attr('value',$('#numberInput19444').val()).autoNumericSet($('#input19444').val()); }
});
if($('#input19444').val()) { $('#numberInput19444').autoNumericSet($('#input19444').val()); }
});
</script>
<script type="text/javascript">
;
 VHV.using ($.extend(
$.parseJSON(decode64('eyJsYXlvdXQiOiJQcm9qZWN0Lk1lZGljYWxQcmljZS5Ib21lLk1lZGljYWxQcmljZS5EcnVnLmxpc3QiLCJpdGVtc1BlclBhZ2UiOjEwLCJ0b3RhbEl0ZW1zIjo2MjQzOCwicGFnZU5vIjoyLCJzZXJ2aWNlIjoiUHJvamVjdC5NZWRpY2FsUHJpY2UuSG9tZS5NZWRpY2FsUHJpY2UuRHJ1Zy5zZWxlY3RBbGwiLCJ3aWRnZXRDb2RlIjoiTXVsdGltZWRpYSIsInR5cGUiOiJNZWRpY2FsUHJpY2UuRHJ1ZyIsInBhdGgiOiJDb250ZW50In0=')),{"module":"Content.Listing","page":"Project.MedicalPrice.Home.MedicalPrice.Drug.list","id":"10","modulePosition":"0","moduleParentId":"-1"}),'LMS.GroupLMSTraining',{ groupId: "", filters: [], options: {"itemsPerPage":10,"pageNo":2,"type":"MedicalPrice.Drug"}, itemsPerPage: 10, totalItems: 62438, menuId:decode64(''), orderBy: "", });
var width = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth; if(width < 768) { $('#region-help-button').append($('.toggle-filter10')); }
$('.toggle-filter10').click(function () { $('.wrap-filter10').toggleClass('active'); })
'''

if __name__=="__main__":
    lst_data = []
    s = soup(text, features='lxml').table

    for tr in  s.findAll("tr"):
        item = {}
        for i, td in enumerate(tr.find_all('td')):
            if i == 1:
                item['medication_name'] = td.text
            elif i == 2:
                item['active_ingredient'] = td.text
            elif i == 5:
                item['packaging'] = td.text
            elif i == 6:
                item['unit'] = td.text
            elif i == 9:
                item['distributor'] = td.text
            elif i == 10:
                item['price'] = td.text

