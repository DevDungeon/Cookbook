#ifndef INIT_HPP_INCLUDED
#define INIT_HPP_INCLUDED

// Globals
GLuint myShaderProgram;
GLuint positionBufferObject;
GLuint vao;



GLuint PerspectiveOffset, VertexOffset; // used to store shader uniform location
GLuint frustumScaleUnif;
GLuint zNearUnif, zFarUnif;

// Loads and compiles shader
GLuint CreateShader(GLenum eShaderType, const std::string &strShaderFile)
{
	GLuint shader = glCreateShader(eShaderType);

	std::ifstream shaderFile(strShaderFile.c_str());
	std::stringstream shaderData;
	shaderData << shaderFile.rdbuf();
	shaderFile.close();
    std::string temp_string = shaderData.str();
    const char *shader_c_str = temp_string.c_str();

	glShaderSource(shader, 1, &shader_c_str, NULL);

	glCompileShader(shader);

	GLint status;
	glGetShaderiv(shader, GL_COMPILE_STATUS, &status);
	if (status == GL_FALSE)
	{
		GLint infoLogLength;
		glGetShaderiv(shader, GL_INFO_LOG_LENGTH, &infoLogLength);

		GLchar *strInfoLog = new GLchar[infoLogLength + 1];
		glGetShaderInfoLog(shader, infoLogLength, NULL, strInfoLog);

		const char *strShaderType = NULL;
		switch(eShaderType)
		{
		case GL_VERTEX_SHADER: strShaderType = "vertex"; break;
		case GL_GEOMETRY_SHADER: strShaderType = "geometry"; break;
		case GL_FRAGMENT_SHADER: strShaderType = "fragment"; break;
		}

		std::cout << "Compile failure in " << strShaderType << " shader: " << strInfoLog << std::endl;
		std::cout << "Make sure the shader files are in the proper location. Try putting shader files in same working directory calling the .exe" << std::endl;
		delete[] strInfoLog;
	}

	return shader;
}


// Attachs shaders, links, detach shaders
GLuint CreateProgram(const std::vector<GLuint> &shaderList)
{
	GLuint program = glCreateProgram();

	for(size_t iLoop = 0; iLoop < shaderList.size(); iLoop++)
		glAttachShader(program, shaderList[iLoop]);

	glLinkProgram(program);

	GLint status;
	glGetProgramiv (program, GL_LINK_STATUS, &status);
	if (status == GL_FALSE)
	{
		GLint infoLogLength;
		glGetProgramiv(program, GL_INFO_LOG_LENGTH, &infoLogLength);

		GLchar *strInfoLog = new GLchar[infoLogLength + 1];
		glGetProgramInfoLog(program, infoLogLength, NULL, strInfoLog);
		std::cout << "Linker failure: " << strInfoLog << std::endl;
		delete[] strInfoLog;
	}

	for(size_t iLoop = 0; iLoop < shaderList.size(); iLoop++)
		glDetachShader(program, shaderList[iLoop]);

	return program;
}


// Create shaders, create program, delete shaders
void InitializeProgram()
{
	std::vector<GLuint> shaderList;


	//shaderList.push_back(CreateShader(GL_VERTEX_SHADER, "VertexPosition.shader"));
shaderList.push_back(CreateShader(GL_VERTEX_SHADER, "ManualPerspective.shader"));
	shaderList.push_back(CreateShader(GL_FRAGMENT_SHADER, "FragmentColor.shader"));



	myShaderProgram = CreateProgram(shaderList);

	std::for_each(shaderList.begin(), shaderList.end(), glDeleteShader);
}


// Init Vertex Buffer with data
void InitializeVertexBuffer()
{
	glGenBuffers(1, &positionBufferObject);
	glBindBuffer(GL_ARRAY_BUFFER, positionBufferObject);
	glBufferData(GL_ARRAY_BUFFER, sizeof(vertexData), vertexData, GL_STREAM_DRAW);
	glBindBuffer(GL_ARRAY_BUFFER, 0);
}


void init() {
    glfwInit();

    glfwOpenWindow(1024, 768, 8, 8, 8, 8, 8, 8, GLFW_WINDOW);

    // Load GL extension functions
    if(glload::LoadFunctions() == glload::LS_LOAD_FAILED)
        std::cout << "error" << std::endl;

    // Initialize shaders and vertex buffers
    InitializeProgram();


PerspectiveOffset = glGetUniformLocation(myShaderProgram, "PerspectiveOffset");
    //VertexOffset = glGetUniformLocation(myShaderProgram, "VertexOffset");

  frustumScaleUnif = glGetUniformLocation(myShaderProgram, "frustumScale");
    zNearUnif = glGetUniformLocation(myShaderProgram, "zNear");
    zFarUnif = glGetUniformLocation(myShaderProgram, "zFar");

    glUseProgram(myShaderProgram);
    glUniform1f(frustumScaleUnif, 1.0f);
    glUniform1f(zNearUnif, 1.0f);
    glUniform1f(zFarUnif, 5.0f);
    glUniform2f(VertexOffset,0.6f, 0.4f);
    glUseProgram(0);




	InitializeVertexBuffer();

	glGenVertexArrays(1, &vao);
	glBindVertexArray(vao);

	//Culling
	glEnable(GL_CULL_FACE);
    glCullFace(GL_BACK);
    glFrontFace(GL_CW);

}

#endif // INIT_HPP_INCLUDED
