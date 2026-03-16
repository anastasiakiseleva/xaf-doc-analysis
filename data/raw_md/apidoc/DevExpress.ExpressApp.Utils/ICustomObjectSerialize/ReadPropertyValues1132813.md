---
uid: DevExpress.ExpressApp.Utils.ICustomObjectSerialize.ReadPropertyValues(DevExpress.ExpressApp.Utils.SettingsStorage)
name: ReadPropertyValues(SettingsStorage)
type: Method
summary: Reads values from the settings storage object.
syntax:
  content: void ReadPropertyValues(SettingsStorage storage)
  parameters:
  - id: storage
    type: DevExpress.ExpressApp.Utils.SettingsStorage
    description: A **SettingsStorage** object representing the storage with values to be read.
seealso: []
---
When implementing the [](xref:DevExpress.ExpressApp.Utils.ICustomObjectSerialize) interface, this method should handle the process of reading values from the specified settings storage object. You can use the **SettingsStorage.LoadOption** method to load a string value, the **SettingsStorage.LoadIntOption** method to load an integer value and the **SettingsStorage.LoadBoolOption** method to load a boolean value.