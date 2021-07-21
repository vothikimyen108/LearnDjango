## Làm việc trên shell  pythonDjango

### Mở đầu
Muốn viết những câu truy vấn trực tiếp, ta sẽ dùng câu lệnh **shell** của **manage.py** để thực tập lần này. Đầu tiên mở **terminal** và chạy câu lệnh sau:

> python manage.py shell
 
 Sau khi chạy xong câu lệnh đó, cần import những cái cần dùng vào ví dụ
 ```python
 >>> from courses.models import *
 ```

 ### Một số cách tương tác
 #### Thêm dữ liệu
**Cách 1**
  ```python
 >>> c = Category(name="Công nghệ Thông tin") 
 >>>> c.save()
 ```
**Cách 2**
 dùng objects phương thức create để tạo thẳng
  ```python
 >>> Category.objects.create(name="lập trình hiện đại")
 ```
 #### một số phương thức phổ biến
 **get_or_create()** lấy nếu thấy tên đó, tạo mới nếu chưa có
  **update_or_create()** update thấy tên đó, tạo mới nếu chưa có/
   ```python
 >>> Category.objects.get_or_create(name="Thiết kế web")
 >>> Category.objects.update_or_create(name="Thiết kế web")
 ```
**thêm dữ liệu có khóa ngoại**
lấy đối tượng đó, pk là viết tắt khóa chính,  xem danh sách thuộc tính đối thượng gọi từ điển ra (.__dict__) sau đó chỉ định khóa ngoại category = c
   ```python
 >>> c = Category.objects.get(pk=1)
 >>> c
 >>> <Category: Category object (1)>
 >>> c.__dict__
{'_state': <django.db.models.base.ModelState object at 0x0000027D9E0D2190>, 'id': 1, 'name': 'lập trình hiện đại'}

>>> Course.objects.create(subject="core python", description="nhập môn hiện đại", category =c)
 ```
  #### Truy vấn dữ liệu
  **Tìm dữ liệu**
  *contains*: chứa không phân biệt hoa thường 
    *icontains*: chứa phân biệt hoa thường 
  ```python
  >>> Course.objects.filter(subject__contains="python")
<QuerySet [<Course: Course object (1)>]>
>>> Course.objects.filter(subject__startswith="python")
<QuerySet []>
>>> Course.objects.filter(subject__endswith="python")
<QuerySet []>
  ```
  
  Khi truy vấn muốn xem câu truy vấn SQL được tạo ra sử dụng đối tượng query như sau:
```python
>>> q = Course.objects.filter(subject__endswith="python")
>>> print(q.query)
SELECT `courses_course`.`id`, `courses_course`.`subject`, `courses_course`.`description`, `courses_course`.`cteate_date`, `courses_course`.`update_date`, `courses_course`.`active`, `cours
es_course`.`category_id` FROM `courses_course` WHERE `courses_course`.`subject` LIKE BINARY %python
```
  **join table**
  Ví dụ lấy tất cả khóa học mà tên danh mục có chữ java liên kết giữa hai bảng course và category ta làm như sau.
  
  ```python
>>> q = Course.objects.filter(category__name__contains="java")
>>> q #xuất ra kết quả
```
