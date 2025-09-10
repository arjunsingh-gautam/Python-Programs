# <span style="color:#003566"> **Notes on Data Members in Python Classes** </span>

## <span style="color:#ffc300"> **Instance Data Members**</span>

- **Definition:** Belong to an **object** (instance). Each object has its own copy.
- **Purpose:** Store specific data unique to each object.
- **Memory:** Created **every time** a new object is created.

### How to Define Instance Data Members

#### 1. Through Constructor

```python
class Student:
    def __init__(self, name, grade):
        self.name = name          # instance data member
        self.grade = grade        # instance data member

s1 = Student("Alice", 10)
s2 = Student("Bob", 12)
print(s1.name, s1.grade)   # Alice 10
print(s2.name, s2.grade)   # Bob 12
```

#### 2. Inside an Instance Method

```python
class Student:
    def set_info(self, name):
        self.name = name   # created only when method is called

s1 = Student()
s1.set_info("Alice")   # now 'name' exists for s1
print(s1.name)         # Alice
```

#### 3. Through an Object (directly)

```python
class Student:
    pass

s1 = Student()
s1.name = "Alice"   # created outside the class!
print(s1.name)      # Alice
```

---

## <span style="color:#ffc300"> 2️⃣ **Class Level Data Members**</span>

- **Definition:** Belong to the **class itself**, not to any single object.
- **Purpose:** Store values that are **common to all objects**.
- **Memory:** Created **only once** when the class is defined.

### How to Define Class Data Members

#### 1. Inside Class Definition

```python
class Student:
    school_name = "Central High"   # class data member

print(Student.school_name)   # access via class name
```

#### 2. Inside a Class Method

```python
class Student:
    school_name = "Central High"

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name   # modify class-level variable

Student.change_school("North High")
print(Student.school_name)   # North High
```

---

## 🔑 Accessing Data Members

- Instance Data Members:

  - `objectname.member`
  - `self.member` (inside methods)

- Class Data Members:

  - `ClassName.member`
  - `objectname.member`
  - `cls.member` (inside class method)
  - `self.member` (inside instance method → though not recommended, because it may confuse readers)

---

## ⚠️ Precautions

### For Instance Data Members

1. Define them **in constructor** (`__init__`) for consistency.

   - If you define them only in some methods, some objects may miss them.
   - Example:

     ```python
     class Student:
         def set_name(self, name):
             self.name = name

     s1 = Student()
     # print(s1.name)   # ❌ AttributeError (not defined yet)
     ```

2. Avoid creating them directly outside the class with `object.attribute = ...`, unless absolutely needed → breaks consistency.

---

### For Class Data Members

1. Be careful: If you modify a class variable using an **object**, it creates a **new instance variable** instead of modifying the class variable.

   ```python
   class Student:
       school = "Central"

   s1 = Student()
   s2 = Student()

   s1.school = "North"   # creates an INSTANCE variable in s1
   print(s1.school)  # North (from instance)
   print(s2.school)  # Central (still from class)
   print(Student.school) # Central
   ```

2. Always modify class variables with `ClassName.variable` or `cls.variable` in class methods.

---

# ✅ Quick Summary

- **Instance Data Members** = unique per object → defined in constructor, instance method, or via object.
- **Class Data Members** = shared by all objects → defined in class body or class method.
- **Precautions:**

  - Stick to constructor for instance members (consistency).
  - Modify class members with `cls` or class name, not via objects.

---
