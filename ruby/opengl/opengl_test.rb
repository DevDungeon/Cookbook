require 'opengl'
require 'glu'
require 'glut'
include Gl,Glu,Glut

# Create a display
display = Proc.new do
  
  # Clear screen
  glClear(GL_COLOR_BUFFER_BIT)

  # Set color for drawing
  glColor(0.0, 0.0, 1.0)

  # Draw a polygon
  glBegin(GL_POLYGON)
  glVertex(0.25, 0.25, 0.0)
  glVertex(0.75, 0.25, 0.0)
  glVertex(0.75, 0.75, 0.0)
  glVertex(0.25, 0.75, 0.0)
  glEnd()

  # Update screen
  glutSwapBuffers()
end

# Initial set up before loop runs
def init
  # Clear and set background color, RGBA
  glClearColor(1.0, 0.0, 0.0, 1)

  # Which matrix is the current matrix:
  # GL_MODELVIEW GL_PROJECTION GL_TEXTURE GL_COLOR
  glMatrixMode(GL_PROJECTION)

  # Replace current matrix with identity matrix
  glLoadIdentity()

  # Multiply current matrix (now the identity matrix) with
  # an orthographic matrix
  # Left, right, bottom, top, nearVal, farVal
  glOrtho(0.0, 1.0, 0.0, 1.0, -1.0, 1.0)
end

# Watch keyboard input for exit key
keyboard = Proc.new do |key, x, y|
  case (key)
    when ?\e
    exit(0);
  end
end

# Get gl ready
glutInit
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(400, 400)
glutCreateWindow("OpenGL Test")
init()
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutMainLoop()
