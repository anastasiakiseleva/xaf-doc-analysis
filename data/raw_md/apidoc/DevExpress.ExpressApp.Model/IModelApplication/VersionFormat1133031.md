---
uid: DevExpress.ExpressApp.Model.IModelApplication.VersionFormat
name: VersionFormat
type: Property
summary: Specifies the format which defines how the application's version is displayed in the [About Information block](xref:113445).
syntax:
  content: string VersionFormat { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string specifying the format which defines how the application's version is displayed in the About Information block.
seealso: []
---
The following format items are applicable:

* {0} - Specifies the application's major version number.
* {1} - Specifies the application's minor version number.
* {2} - Specifies the application's revision version number.
* {3} - Specifies the application's build version number.