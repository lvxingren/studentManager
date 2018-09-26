from app import db

#继承了db.Model的类叫做数据模型类
#这个类将来在数据库中对应一张表，类改变了表就改变了
#类中的每一个子段在表中对应一个属性（列）
class Student(db.Model) :
	#指定表名
	__tablename__ = 'students'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64))
	age = db.Column(db.Integer)
	sex = db.Column(db.String(64))
	teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))

	#在这里其实还有一个字段叫做bteacher

class Teacher(db.Model) :
	__tablename__ = 'teachers'
	#主键
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64))
	age = db.Column(db.Integer)

	#反向关系：
	#1.在这里添加一个字段叫做students
	#2.在学生类中添加一个字段叫做bteacher
	#3.但，这两个字段都不会出现在数据库中，之后在对象中，方便编程
	students = db.relationship('Student', backref='teacher', lazy='dynamic')
	#理由1：本来就存在一对多的关系  bteachers.id------>students.b_id
	#理由2：一个老师可以对多个学生 所以在老师类加students表示所有学生
	#理由3：一个老师可以对多个学生 所以在学生类加bteacher表示学生的老师
	




