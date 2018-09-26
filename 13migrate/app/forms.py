from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, IntegerField
from wtforms import SubmitField
from wtforms.validators import DataRequired, Length, Email
from wtforms.validators import EqualTo

class AddStudentForm(FlaskForm) :
	#为了安全要进行表单验证
	name = StringField(label='名字', validators=[DataRequired(), Length(1, 64)])
	age = IntegerField(label='年龄')
	sex = IntegerField(label='性别')
	teacher_name = StringField(label='班主任', validators=[DataRequired(), Length(1, 64)])
	submit = SubmitField(label='提交')

class AddTeacherForm(FlaskForm) :
        #为了安全要进行表单验证
	name = StringField(label='名字', validators=[DataRequired(), Length(1, 64)])
	age = IntegerField(label='年龄')
	submit = SubmitField(label='提交')

