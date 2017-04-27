
RelightingWizardTool.actionOpenProject("../relighting_projects/matthias_ruether/new_project.rel_proj");
RelightingWizardTool.actionImportFrames("../raw_data/matthias_ruether/undistortedImages");

RelightingWizardTool.actionPlayFrames();

RaytracerTool.actionFocusCameraOnMesh()

mtp = Item("MultiTextureProjectorHandle")
mtp.FOVH = 85;
mtp.FOVV = 56;

