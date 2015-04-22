#version 330

out vec4 outputColor;

void main()
{
	float lerpValue = gl_FragCoord.y / 5000.0f;

	outputColor = mix(vec4(0.70f, 0.0f, 0.0f, 1.0f), vec4(0.0f, 1.0f, 0.2f, 1.0f), lerpValue);
}
