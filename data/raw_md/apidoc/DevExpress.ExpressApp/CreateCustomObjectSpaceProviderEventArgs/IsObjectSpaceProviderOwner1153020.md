---
uid: DevExpress.ExpressApp.CreateCustomObjectSpaceProviderEventArgs.IsObjectSpaceProviderOwner
name: IsObjectSpaceProviderOwner
type: Property
summary: Specifies whether or not the Object Space Provider is disposed of when the application is disposed of.
syntax:
  content: public bool IsObjectSpaceProviderOwner { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if the Object Space Provider is disposed of together with the application; otherwise, **false**.'
seealso: []
---
When Object Space Providers are created using the [XafApplication.CreateCustomObjectSpaceProvider](xref:DevExpress.ExpressApp.XafApplication.CreateCustomObjectSpaceProvider) event, providers and their connections are disposed of together with their application (e.g., on re-logon). Set the **IsObjectSpaceProviderOwner** parameter to **false** to cancel disposal of providers together with the application in this scenario

# [C#](#tab/tabid-csharp)

```csharp
private void Instance_CreateCustomObjectSpaceProvider(object sender, CreateCustomObjectSpaceProviderEventArgs e) {
    IXpoDataStoreProvider dataStoreProvider = null;
    if(Application["DataStoreProvider"] != null) {
        dataStoreProvider = Application["DataStoreProvider"] as IXpoDataStoreProvider;
        e.ObjectSpaceProvider = new SecuredObjectSpaceProvider((ISelectDataSecurityProvider)WebApplication.Instance.Security, dataStoreProvider, true);
    }
    else {
        if(!String.IsNullOrEmpty(e.ConnectionString)) {
            string connectionString = DevExpress.Xpo.XpoDefault.GetConnectionPoolString(e.ConnectionString);
            dataStoreProvider = new ConnectionStringDataStoreProvider(connectionString, true);
        }
        else if (e.Connection != null){
            dataStoreProvider = new ConnectionDataStoreProvider(e.Connection);
        }
        Application["DataStoreProvider"] = dataStoreProvider;
        e.ObjectSpaceProvider = new SecuredObjectSpaceProvider((ISelectDataSecurityProvider)WebApplication.Instance.Security, dataStoreProvider, true);
    }
    e.IsObjectSpaceProviderOwner = false;
}
```
***