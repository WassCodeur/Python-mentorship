from models.base import Base

class Rectangle(Base):
	
	def __init__(self, width, height, x=0, y=0, id=None):
		super().__init__(id)
		self.width = width 
		self.height = height
		self.x = x
		self.y = y
		
	@property
	def width(self):
		return self.__width
    
	@width.setter
	def width(self, value):
		if type(value) != int:
			raise TypeError('width must be a integer')
		if value <= 0:
			raise ValueError('width must be > 0')
		self.__width = value

	@property
	def height(self):
		return self.__height

	@height.setter
	def height(self, value):
		if type(value) != int:
			raise TypeError('height must be a integer')
		if value <= 0:
			raise ValueError('height must be > 0')
		self.__height = value	

	@property
	def x(self):
		return self.__x
	
	@x.setter 
	def x(self, value):
		if not isinstance(value, int):
			raise TypeError('x must be a integer')
		if value <= 0:
			raise ValueError('x must be > 0')
		self.__x = value

	@property
	def y(self):
		return self.__y

	@y.setter 
	def y(self,value):
		if not isinstance(value,int):
			raise TypeError('y must be a integer')
		if value <= 0:
			raise ValueError('y must be > 0')
		self.__y = value
	
	def area(self):
		return self.height * self.width
	def display(self):
		for _ in range(self.height):
			for _ in range(self.width):
				print('#', end ="")
			print()	

		
		