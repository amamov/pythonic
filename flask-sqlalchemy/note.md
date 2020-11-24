# flask-sqlalchemy

```python
class User(db.Model):
    __tablename__ = "amamov_user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(120), nullable=False)

```

## CRUD

1. Create

```python
amamov = User(username='yss', email='ysangsuk78@gmail.com') # user 객체 생성
spring = User(username='spring', email='email@spring')
summer = User(username='summer', email='email@summer')
tokyo = User(username='tokyo', email='email@tokyo')
seoul = User(username='seoul', email='email@seoul')

db.session.add(amamov)
db.session.commit()

db.session.add_all([spring, summer, tokyo, seoul]) # 리스트로 한 번에 add
db.session.commit()
```

2. Read

```python
## User table의 모든 객체를 list 형태로 가져온다.
User.query.all()
# >> [<User amamov>, <User spring>, <User summer>, <User tokyo>, <User seoul>]

## User table의 username이 tokyo인 객체들중 첫 번째 데이터을 가져온다.
User.query.filter(User.username=='tokyo').first()
```

3. Update

```python
## 방법 1
t = User.query.filter(User.username=='tokyo').first()

print(t.email)
# 'email@tokyo'

## 값 수정
t.email = 'email@ttt'
db.session.commit()

## 업데이트 확인
print(t.email)
# 'email@ttt'

## 방법 2
uid = 1 # 업데이트 대상 객체의 id를 알고 있다고 하자.

updated_data={'email': 'email@amamovamamov'}

# User.id 가 uid인 객체를 업데이트한다.
a = User.query.filter(User.id==uid).update(updated_data)
db.session.commit(a)
```

4. Delete

```python
# User.query.filter(User.id == uid).first() ===  User.query.get(uid)

uid = 1 # 제거 대상 객체의 id를 알고 있다고 하자.
a = User.query.filter(User.id == uid).delete()
db.session.commit()

b = User.query.get(2)
db.session.delete(b)
db.session.commit()
```

---

## Query

### 1. User.query.filter(User.id != 1).all()

- User table의 객체들중 id가 1이 아닌 모든 객체들을 리스트로 가져온다.

### 2. User.query.filter(User.email.like("%gmail%")).all()

- User table의 객체들중 email에 gmail이라는 단어(문자열)이 존재하는 모든 객체들을 리스트로 가져온다.

### 3. User.query.filter(User.username.in\_(['spring', 'fall', 'amamov'])).all()

- User table의 객체들중 ['spring', 'fall', 'amamov']에 속하는 username인 객체들을 모두 리스트로 가져온다.

### 4. User.query.filter(~User.username.in\_(['spring', 'fall', 'amamov'])).all()

- User table의 객체들중 ['spring', 'fall', 'amamov']에 속하지 않는 username인 객체들을 모두 리스트로 가져온다.

### 5. User.query.filter(User.email == None).all()

    - User table의 객체들중 email 이 없는 객체들을 모두 리스트로 가져온다.

### 6. User.query.filter(db.and\_(User.username.like('%s%), User.email.like('%gmail%))).all()

    - User table의 객체들중 username에 s가 들어가고 email에 gmail이 들어가는 모든 객체를 리스트로 가져온다.
    - User.query.filter(User.username.like('%s%')).filter(User.email.like('%gmail%')).all() 과 같다.

### 7. User.query.filter(db.or\_(User.username.like('%s%), User.email.like('%gmail%))).all()

    - User table의 객체들중 username에 s가 들어가거나 또는 email에 gmail이 들어가는 모든 객체를 리스트로 가져온다.

### 8. User.query.order_by(User.username).all()

    - User table의 객체들을 username 오름차순으로 정렬하여 리스트로 모두 가져온다.
    - User.query.filter(...).order_by(...) 으로 주로 사용
    - 오름차순이란 작은 것부터 큰 순서로 정렬하는 방식이다.
    - abcdef.., 12345...
    - 내림차순으로 정렬하고 싶다면 User.query.order_by(User.username.desc()).all()로 사용한다.

### 9. User.query.limit(3).all()

    - User table의 객체들을 3개만 리스트로 모두 가져온다.
    - User.query.filter(...).limit(...) 으로 주로 사용

### 10. User.query.offset(3).all()

    - User table의 객체들중 3개를 건너뛰고 나머지를 리스트로 모두 가져온다.
    - User.query.filter(...).offset(...) 으로 주로 사용
    - 만약 User.query.all()이 [<User 'spring'>, <User 'amamov'>, <User 'fall'>, <User 'joy'>, <User 'yua'>]라면 [<User 'joy'>, <User 'yua'>]만 가져온다.
    - limit와 같이 써서 pagination을 구현할 수 있다.

### 11. User.query.filter(User.password == password).count()

    - User table의 객체들중 조건에 성립하는 객체 수를 반환한다.

---

## Relationship
