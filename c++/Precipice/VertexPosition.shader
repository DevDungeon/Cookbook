#version 330

layout(location = 0) in vec4 position;
uniform vec2 VertexOffset;

void main()
{
	vec4 totalOffset = vec4(VertexOffset.x, VertexOffset.y, 0.0, 0.0);
	gl_Position = position + totalOffset;
}
