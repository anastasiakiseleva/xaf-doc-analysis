---
uid: DevExpress.Persistent.BaseImpl.BaseObject.OidInitializationMode
name: OidInitializationMode
type: Property
summary: Specifies when a new GUID value is assigned to the [BaseObject.Oid](xref:DevExpress.Persistent.BaseImpl.BaseObject.Oid) property.
syntax:
  content: public static OidInitializationMode OidInitializationMode { get; set; }
  parameters: []
  return:
    type: DevExpress.Persistent.BaseImpl.OidInitializationMode
    description: An [](xref:DevExpress.Persistent.BaseImpl.OidInitializationMode) enumeration value specifying when a new GUID value is assigned to the Oid property.
seealso: []
---
In [OidInitializationMode.AfterConstruction](xref:DevExpress.Persistent.BaseImpl.OidInitializationMode.AfterConstruction) mode, the unique object identifier is immediately assigned to a newly created object. In [OidInitializationMode.OnSaving](xref:DevExpress.Persistent.BaseImpl.OidInitializationMode.OnSaving) mode, the unique identifier is assigned to a newly created object when the object is saved.

The [Template Kit](xref:405447) generates new projects with the [FrameworkSettings.DefaultSettingsCompatibilityMode](xref:DevExpress.ExpressApp.FrameworkSettings.DefaultSettingsCompatibilityMode) property set to `Latest`. This sets the `OidInitializationMode` property value to `AfterConstruction` using the following code line added to the [](xref:DevExpress.ExpressApp.ModuleBase) constructor in the [!include[File_Module](~/templates/file_module11171.md)] file:

# [C#](#tab/tabid-csharp)

```csharp
BaseObject.OidInitializationMode = OidInitializationMode.AfterConstruction;
```
***

