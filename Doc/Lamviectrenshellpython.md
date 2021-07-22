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
 Dùng objects phương thức create để tạo thẳng.
 
 Để truy vấn CSDL, ta tạo QuerySet thông qua Manager trên lớp model. Mỗi model có ít nhất một Manager gọi là objects. Một QuerySet đại diện cho nhiều đối tượng từ CSDL. 
 
 QuerySet là lazy, tức là khi tạo QuerySet nó chưa thực sự truy vấn xuống CSDL, cho đến khi có một lệnh nào đó yêu cầu thực hiện (evaluated)
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
  **Thêm dữ liệu many to many**
   ```python
>>> l = Lesson.objects.get(pk=1) #lấy bài học số 1
>>>	t = Tag.objects.create(name="python") #tạo tag mới
>>> l.tags.add(t)
>>> l.save() #tự nó thêm 2 khóa ngoại vô bản trung gian lesson_tag
 ```
  #### Truy vấn dữ liệu
  **Tìm dữ liệu**
  dùng filter lọc có điều kiện
 **Một số field lookups chỉ định điều kiện**
    **exact** và **iexact** (so sánh chính xác)
     **contains** và  **icontains**
    **in** (trong)
     **gt**(lớn hơn), **gte**(lớn hơn bằng)
    **lt**(nhỏ hơn) , **lte**(nhỏ hơn bằng), 	**ange**(between)
    **startswith**(bắt đầu với), **istartswith**, **endswith**, **iendswith**
     **i**(là không phân biệt hoa thường)
    **regex**,** iregex**(truy vấn biểu thức chính quy)
   **date, year, month, day, hour, minute, second**
  ```python
  >>> Course.objects.filter(subject__contains="python")
<QuerySet [<Course: Course object (1)>]>
>>> Course.objects.filter(subject__startswith="python")
<QuerySet []>
>>> Course.objects.filter(subject__endswith="python")
<QuerySet []>
Course.objects.filter(created_date__year=2021) # Lấy khóa học có năm tạo 2021
  ```
   dùng exclude bỏ ra những cái thỏa điều kiện đó.
  ```python
Course.objects.exclude(created_date__year__lte=2020)
```
Mặc định các điều kiện trong filter hoặc exclude sẽ liên kết bằng phép AND. Để thực hiện các truy vấn phức tạp hơn sử dụng Q(). Các Q có thể kết hợp với nhau bằng phép & hoặc .
>from django.db.models import Q

```python
>>>from django.db.models import Q
>>>Course.objects.filter(Q(created_date__year=2020)| Q(subject__icontains='lập trình')) #kết nhau bới mệnh đề or
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
Trong khóa học có những bài học nào theo cách dưới đấy hướng đối tượng
```python
>>> c= Course.objects.get(pk=1) #lây khóa học có khóa chính 1
>>> c.lessons.all() #lấy khóa học đó xem có bài học nào c.lesson_set.all() mặc định nếu chưa đổi  related_name
<QuerySet [<Lesson: intro to python>]>
```
  **truy vấn dữ liệu many to many**
  Xem danh sách Lesson của Tag và ngược lại.
  ```python
>>> t = Tag.objects.create(name="python") #tạo tag mới
>>> t.lessons.all() #tag đó có bao nhiêu bài học
<QuerySet [<Lesson: intro to python>]>
```
  **Một số truy vấn thông dùng**
 • **count()**: số đối tượng trong QuerySet.
 • **latest()**: trả về đối tượng cuối trong QuerySet dựa trên trường chỉ định. 
 • **earliest()**: ngược lại với latest() 
 • **first()**: trả về đối tượng đầu tiên trong QuerySet 
 • **last()**: trả về đối tượng cuối trong QuerySet 
 • **exists()**: kiểm tra QuerySet có tồn tại kết quả nào không. 
 • **aggregate()**: thống kê cho QuerySet (sum, max)
  •**order_by()**: thực hiện sắp xếp, mặc định QuerySet sắp xếp dựa trên thuộc tính ordering trong Meta của model, ta cũng có thể ghi đè bằng cách sử dụng order_by().
 
 ```python
 >>> Lesson.objects.latest("cteate_date") #bài học tạo ra cuối cùng
<Lesson: intro to python>
>>> Course.objects.order_by('category_id', '-id')
<QuerySet [<Course: core java>]> #c giảm dần theo mã danh mục, nếu cùng mã danh mục thì tăng dần theo id khoá học
 ```
