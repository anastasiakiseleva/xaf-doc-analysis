---
uid: DevExpress.ExpressApp.Utils.ImageLoader.LoadFromResource(System.Reflection.Assembly,System.String)
name: LoadFromResource(Assembly, String)
type: Method
summary: Retrieves an image stored as a resource in an assembly.
syntax:
  content: |-
    [Browsable(false)]
    public DXImage LoadFromResource(Assembly assembly, string resourceName)
  parameters:
  - id: assembly
    type: System.Reflection.Assembly
    description: The assembly from which the image is loaded.
  - id: resourceName
    type: System.String
    description: The name of the resource that contains the image.
  return:
    type: DevExpress.Drawing.DXImage
    description: The retrieved image.
seealso:
- linkId: "112792"
---
This method is intended for internal use.