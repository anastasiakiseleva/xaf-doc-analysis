---
uid: DevExpress.ExpressApp.Utils.ImageLoader.LoadFromFullResource(System.Reflection.Assembly,System.String)
name: LoadFromFullResource(Assembly, String)
type: Method
summary: Retrieves an image stored as a resource in an assembly.
syntax:
  content: |-
    [Browsable(false)]
    public DXImage LoadFromFullResource(Assembly assembly, string fullResourceName)
  parameters:
  - id: assembly
    type: System.Reflection.Assembly
    description: The assembly from which the image is loaded.
  - id: fullResourceName
    type: System.String
    description: The full name of the resource that contains the image.
  return:
    type: DevExpress.Drawing.DXImage
    description: The retrieved image.
seealso:
- linkId: "112792"
---
This method is intended for internal use.