
class Complex :

   def __init__( self, re, im = 0 ) :
      self.re = re
      self.im = im

   def __repr__( self ) :
      return "{} + {}i".format( self. re, self.im )

   def __add__( self, other ) : 
      if not isinstance( other, Complex ):
         return Complex( self. re + other, self. im ) 
      else: 
         return Complex( self. re + other. re, self. im + other. im ) 

   def __radd__( self, other ) :
      return self.__add__( other ) 

   def __sub__( self, other ) :
      if not isinstance( other, Complex ):
         return Complex( self. re - other, self. im )
      else:
         return Complex( self. re - other. re, self. im - other. im )

   def __rsub__( self, other ) :
      if not isinstance( other, Complex ):
         return Complex( other - self. re, -self. im )
      else:
         return Complex( other. re - self. re, other. im - self. im )

   def __mul__( self, other ) :
      if not isinstance( other, Complex ) :
         return Complex( other * self.re, other * self. im )
      else :
         return Complex( self.re * other.re - self.im * other. im,
                         self.re * other.im + self.im * other.re )

   def __rmul__( self, other ) :
      return self.__mul__( other )

   def __imul__( self, other ) :
      if not isinstance( other, Complex ) :
         self.re = self.re * other
         self.im = self.im * other
         return self 
      else :
         raise NotImplemented( ) 
   
   def __iadd__( self, other ) :
      if not isinstance( other, Complex ) :
         other = Complex( other, 0 )

      self. re += other. re
      self. im += other. im
      return self

   def __eq__( self, other ) : 
      if not isinstance( other, Complex ) :
         other = Complex( other, 0 )
      
      return self. re == other. re and self.im == other. im

   def __hash__( self ) :
      return hash( (self.re, self.im) ) 
 
