---
uid: "403958"
title: Connect to an XPO Middle Tier Server from Non-XAF Applications (.NET)
seealso:
  - linkId: "118741"
---

# Connect to an XPO Middle Tier Server from Non-XAF Applications (.NET)

This topic demonstrates how to access the data protected with the [Middle Tier Application Server](xref:403572) from a non-XAF application.


## Initialize Metadata for Persistent Classes

The code sample below demonstrates how to initialize metadata on `Employee`, `Project`, and `Task` persistent classes.

# [C#](#tab/tabid-csharp)

```csharp
XPDictionary dictionary = new ReflectionDictionary();
Type[] types = { typeof(Employee), typeof(Project), typeof(Task) }
dictionary.CollectClassInfos(types);
```
***

You can collect metadata for all persistent classes automatically when your data model is in a separate assembly. The code sample below demonstrates how to collect metadata for all persistent classes in the assembly that contains the _Employee_ class:

# [C#](#tab/tabid-csharp)

```csharp
dictionary.CollectClassInfos(Assembly.GetAssembly(typeof(Employee)));
```
***

## Establish a Connection

The code sample below demonstrates how to create a connection to a Middle Tier Server.

# [C#](#tab/tabid-csharp)

```csharp
var httpClient = new HttpClient();
httpClient.BaseAddress = new Uri("https://localhost:44319/");
var webSocketFactory = new ClientWebSocketFactory(httpClient, false);
var securedClient = new WebSocketSecuredDataServerClient(httpClient, webSocketFactory, XafTypesInfo.Instance);
```
***

## Check if a Permission is Granted

Before checking whether a permission is granted, authenticate at the Middle Tier Service level:

# [C#](#tab/tabid-csharp)

```csharp
securedClient.Authenticate(new AuthenticationStandardLogonParameters("John", ""));
((IMiddleTierServerSecurity)securedClient).Logon();
```
***

When the secured client is initialized, and the user is logged on, you can create a permission request and check whether a user has a specific permission:

# [C#](#tab/tabid-csharp)

```csharp
var readRequest = new SerializablePermissionRequest(typeof(Employee), null, null, SecurityOperations.Read);
bool isReadGranted = ((IMiddleTierServerSecurity)securedClient).IsGranted(readRequest);

var writeRequest = new SerializablePermissionRequest(typeof(Employee), null, null, SecurityOperations.Write);
bool isWriteGranted = ((IMiddleTierServerSecurity)securedClient).IsGranted(writeRequest);
```

***

## Access Data

To access data through the secured Object Access Layer, create a [](xref:DevExpress.Xpo.UnitOfWork) through the constructor that takes an object layer (see [UnitOfWork](xref:DevExpress.Xpo.UnitOfWork.#ctor*)). You can then create an [](xref:DevExpress.Xpo.XPCollection) in this Unit of Work, or use [](xref:DevExpress.Xpo.UnitOfWork) methods. Note that an exception is thrown when you access data that is restricted to the current user.

# [C#](#tab/tabid-csharp)

```csharp
MiddleTierSerializableObjectLayerClient securedObjectLayerClient = new MiddleTierSerializableObjectLayerClient(securedClient);
SerializableObjectLayerClient objectLayerClient = new SerializableObjectLayerClient(securedObjectLayerClient, dictionary);
UnitOfWork uow = new UnitOfWork(objectLayerClient);
foreach (Task task in new XPCollection<Task>(uow)) {
    Console.WriteLine(task.Subject);
}
try {
    var task = uow.Query<Task>().FirstOrDefault(t => t.Subject == "Check Reports");
    task.Subject = "Review Reports";
    uow.CommitChanges();
}
catch (Exception e) {
    Console.WriteLine("Error: " + e.Message);
}
```
***
