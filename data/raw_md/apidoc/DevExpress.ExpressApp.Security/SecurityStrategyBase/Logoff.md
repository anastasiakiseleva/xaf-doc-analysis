---
uid: DevExpress.ExpressApp.Security.SecurityStrategyBase.Logoff
name: Logoff()
type: Method
summary: Logs the current user off.
syntax:
  content: public virtual void Logoff()
seealso: []
---
The following example demonstrates how to use this method in a non-XAF console application:

# [C#](#tab/tabid-csharp)

[!codesnippet-cs{31}[dx-examples](XAF_Security_E4908/XPO/Console/Program.cs?line=1-29,45)]
```cs{31}
using System.Configuration;
using System.Diagnostics;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Security;
using DevExpress.ExpressApp.Security.ClientServer;
using DevExpress.ExpressApp.Xpo;
using DevExpress.Persistent.BaseImpl.PermissionPolicy;
using BusinessObjectsLibrary.BusinessObjects;
using DatabaseUpdater;
using DevExpress.ExpressApp.DC;
using DevExpress.ExpressApp.DC.Xpo;

// ## Step 0. Preparation. Create or update database
TypesInfo typesInfo = new TypesInfo();
RegisterEntities(typesInfo);
string connectionString = ConfigurationManager.ConnectionStrings["ConnectionString"].ConnectionString;
IXpoDataStoreProvider dataStoreProvider = XPObjectSpaceProvider.GetDataStoreProvider(connectionString, null);
CreateDemoData(typesInfo, dataStoreProvider);

// ## Step 1. Initialization. Create a Secured Data Store and Set Authentication Options
AuthenticationStandard authentication = new AuthenticationStandard();
SecurityStrategyComplex security = new SecurityStrategyComplex(typeof(PermissionPolicyUser), typeof(PermissionPolicyRole), authentication, typesInfo);
security.RegisterXPOAdapterProviders();
SecuredObjectSpaceProvider objectSpaceProvider = new SecuredObjectSpaceProvider(security, dataStoreProvider, typesInfo, null);

// ## Step 2. Authentication. Log in as a 'User' with an Empty Password
authentication.SetLogonParameters(new AuthenticationStandardLogonParameters(userName: "User", password: string.Empty));
IObjectSpace loginObjectSpace = objectSpaceProvider.CreateObjectSpace();
security.Logon(loginObjectSpace);
// ...
security.Logoff();
```

***