---
uid: DevExpress.Persistent.Base.ISupportFullName.FullName
name: FullName
type: Property
summary: Gets or sets a full path to the file specified by the object which implements the [](xref:DevExpress.Persistent.Base.IFileData) interface.
syntax:
  content: string FullName { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string that is a full path to the file.
seealso: []
---
To use the **FullName** property, implement the **ISupportFullName** interface in your class in addition to **IFileData**. This property is set to the files full path before the [IFileData.LoadFromStream](xref:DevExpress.Persistent.Base.IFileData.LoadFromStream(System.String,System.IO.Stream)) method is called.