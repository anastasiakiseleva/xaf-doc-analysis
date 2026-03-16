---
uid: DevExpress.ExpressApp.XafApplication.CreateCustomLogonParameterStore
name: CreateCustomLogonParameterStore
type: Event
summary: Occurs both when reading and writing the last logon parameters, before creating the logon parameters storage.
syntax:
  content: public event EventHandler<CreateCustomLogonParameterStoreEventArgs> CreateCustomLogonParameterStore
seealso:
- linkId: DevExpress.ExpressApp.XafApplication.LastLogonParametersReading
- linkId: DevExpress.ExpressApp.XafApplication.LastLogonParametersRead
- linkId: DevExpress.ExpressApp.XafApplication.LastLogonParametersWriting
- linkId: DevExpress.ExpressApp.Utils.ICustomObjectSerialize
---
A logon Window contains a [View](xref:112611), which represents a [Security System](xref:113366)'s logon parameters. By default, this View shows the last user's parameters. To save and load these parameters, a special storage is created. The storage which is used in a Windows Forms application saves (or loads) parameters to the _LogonParameters_ file. ASP.NET Core Blazor applications do not store the last user's logon parameters anywhere. You can customize the default behavior by using another storage. For this purpose, handle the `CreateCustomLogonParameterStore` event. In the handler, create the required storage. The following storage types are available:

| Class | Storage |
|---|---|
| `NullSettingsStorage` | Logon parameters are not saved anywhere, and consequently, are not loaded from anywhere. |
| `SettingsStorageOnHashtable` | Hash table. |
| `SettingsStorageOnRegistry` | Registry. |
| `SettingsStorageOnDictionary` | _LogonParameters_ file. Used in a Windows Forms application. |

Assign the storage you have created to the handler's [CreateCustomLogonParameterStoreEventArgs.Storage](xref:DevExpress.ExpressApp.CreateCustomLogonParameterStoreEventArgs.Storage) parameter.

To prohibit the creation of the default storage object, set the handler's `Handled` parameter to `true`.