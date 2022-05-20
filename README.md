## Install Tor  va Privoxy 
http://akul.me/blog/2017/proxy-cheatsheet/

## Huong dan chi tiet
https://colab.research.google.com/drive/1yRDLKHbxx_n_eAxzvOpWqH--gRRKTVdj?usp=sharing

## Thong tin Database

DATABASE URI: mongodb://admin:admin@54.150.126.18:27017
username/password: admin/admin
DATABASE: CRAWL_MEDICATION_DATA

### Thong tin Collection 

#### Crawl nha thuoc An Khang 
COLLECTION: NHATHUOCANKHANG {
    id: char 
    medication_name: varchar
    image_link_1: char    #link_img    
    image_link_2: char    #link_img    
    packaging:  char
    active_ingredient: varchar
    disease_group: varchar
    manufacterer: varchar 
    manufacterer_location: varchar
    effect: varchar # tác dụng 
    side_effect: varchar # tác dụng phụ 
    contraindication: text  # chong chi dinh 
    dosage: varchar
    price: varchar 
    drugstore_name: varchar
}

#### Crawl DRUGBANK
COLLECTION: DRUGBANK {
    id: char
    tenThuoc: varchar 
    soQuyetDinh: varchar
    soDangKy: varchar 
    hoatchat: varchar 
    phanLoai: varchar 
    nongDo: varchar
    taDuoc: varchar 
    baoChe: varchar 
    dongGoi: varchar 
    tieuChuan: varchar 
    tuoiTho: varchar 
    congtySx: varchar 
    congTySxCode: varchar
    nuocSx: varchar
    diaChiSx: varchar 
    congTyDk: varchar 
    nuocDk: varchar 
    diaChiDk: varchar 
    giaKeKhai: varchar 
    nhomThuoc: varchar 
}

#### Crawl CONGKHAIYTE
COLLECTION: CONGKHAIYTE {
    medication_name: varchar 
    active_ingredient: varchar 
    packaging: varchar 
    unit: varchar 
    distributor: varchar 
    price: varchar
}