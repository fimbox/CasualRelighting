import os  

ROOT_FOLDER = '../relighting_projects/fruit_table_projected'
INPUT_FOLDER = ROOT_FOLDER
OUTPUT_FOLDER = ROOT_FOLDER + '/py_results'

SCREENSHOT_VIEW = "-0,260829061 0,2491733 0,976253152"

cam = Item("Camera")
cam.Fov = 40

def screenshotMesh(mesh_name, path):
	RaytracerTool.actionSelectMesh(mesh_name, "hideothers")
	RaytracerTool.actionFocusCameraOnMesh(SCREENSHOT_VIEW)
	RaytracerTool.actionDeselectMesh()
	RaytracerTool.actionSaveScreenshot(path, 1920,1280)
	
def solveMesh( mesh_path ):
	print("solving " + mesh_path)
	
	RaytracerTool.actionClearAllMeshes();
	RaytracerTool.actionCreateTextureProjector()
	mtp = Item("MultiTextureProjectorHandle")
	mtp.onLoadAverageMesh(mesh_path)
	
	BaseTool.actionExecuteScript(ROOT_FOLDER + "/specular_solving_average_py.tscript")
	
	# for convienient viewing:
	RaytracerTool.EnableRealtimeVertexSH = True
	
	prefix_output = os.path.basename(mesh_path).replace(".bin_mesh","")
	
	output_folder = OUTPUT_FOLDER + "/" + prefix_output
	
	if not os.path.exists(output_folder+"/"):
		os.makedirs(output_folder+"/")
		
	RaytracerTool.actionSaveEnvironmentToCrossFile(output_folder + "/hdr_cross.png" )
	RaytracerTool.actionSaveEnvironmentToSphereFile(output_folder + "/hdr_sphere.png" )
	
	# RaytracerTool.actionClearHDR("white")
	
	screenshotMesh("Mesh Base Mesh", output_folder+"/input.png")
	screenshotMesh("Mesh Plain Lit Mesh", output_folder+"/shade.png")
	screenshotMesh("Mesh Albedo Fin Mesh", output_folder+"/albedo.png")
	screenshotMesh("Mesh Relighten Mesh", output_folder+"/relit.png")
	screenshotMesh("Mesh Segment Mesh", output_folder+"/segments.png")



solveMesh( INPUT_FOLDER + "/improved_average.bin_mesh" )
# solveMesh( INPUT_FOLDER + "/raw_bunny_white_hdr.bin_mesh" )
	

	