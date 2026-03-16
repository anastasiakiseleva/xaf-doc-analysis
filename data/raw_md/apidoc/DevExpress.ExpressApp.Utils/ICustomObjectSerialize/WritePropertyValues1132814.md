---
uid: DevExpress.ExpressApp.Utils.ICustomObjectSerialize.WritePropertyValues(DevExpress.ExpressApp.Utils.SettingsStorage)
name: WritePropertyValues(SettingsStorage)
type: Method
summary: Writes values to the settings storage object.
syntax:
  content: void WritePropertyValues(SettingsStorage storage)
  parameters:
  - id: storage
    type: DevExpress.ExpressApp.Utils.SettingsStorage
    description: A **SettingsStorage** object representing the storage for the values.
seealso: []
---
When implementing the [](xref:DevExpress.ExpressApp.Utils.ICustomObjectSerialize) interface, this method should handle the process of writing values to the specified settings storage object. You can use the **SettingsStorage.SaveOption** method to save a string value. To save a value of another type, covert it to the string representation first.