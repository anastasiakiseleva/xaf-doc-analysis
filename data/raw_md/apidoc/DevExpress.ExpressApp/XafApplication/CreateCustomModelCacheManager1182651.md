---
uid: DevExpress.ExpressApp.XafApplication.CreateCustomModelCacheManager
name: CreateCustomModelCacheManager
type: Event
summary: Occurs when the object used to manage saving and loading the Application Model cache is created.
syntax:
  content: public event EventHandler<CreateCustomModelCacheManagerEventArgs> CreateCustomModelCacheManager
seealso: []
---
By default, the Application Model content is cached to the _Model.Cache.xafml_ file when the [XafApplication.EnableModelCache](xref:DevExpress.ExpressApp.XafApplication.EnableModelCache) property is set to **true**. To use a custom storage for the cache, handle the **CreateCustomModelCacheManager** event and pass a custom [](xref:DevExpress.ExpressApp.ModelCacheManager) object to the [CreateCustomModelCacheManagerEventArgs.ModelCacheManager](xref:DevExpress.ExpressApp.CreateCustomModelCacheManagerEventArgs.ModelCacheManager) parameter.

> [!TIP]
> To change the cache file location, override the **XafApplication.GetModelCacheFileLocationPath** method instead of using this event.

The following example demonstrates the custom **ModelCacheManager** implementation.

# [C#](#tab/tabid-csharp)

```csharp
using System.Collections.Generic;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;
// ...
public class MyModelCacheManager : ModelCacheManager {
    string fileName = "MyCacheFile.bin";
    public MyModelCacheManager() : base(null, AppDomain.CurrentDomain.SetupInformation.ApplicationBase) { }
    public MyModelCacheManager(Stream stream, string modelCacheFileLocationPath)
        : base(stream, modelCacheFileLocationPath) {
    }
    protected override bool CanLoadModelCache() {
        return File.Exists(fileName);
    }
    protected override IDictionary<string, string> LoadCore() {
        Dictionary<string, string> serializedModel = null;
        using (FileStream loadStream = new FileStream(fileName, FileMode.Open, FileAccess.Read)) {
            BinaryFormatter bf = new BinaryFormatter();
            serializedModel = bf.Deserialize(loadStream) as Dictionary<string, string>;
        }
        return serializedModel;
    }
    protected override void SaveCore(Dictionary<string, string> serializedModel) {
        using (FileStream saveStream = new FileStream(fileName, FileMode.OpenOrCreate, FileAccess.ReadWrite)) {
            BinaryFormatter bf = new BinaryFormatter();
            bf.Serialize(saveStream, serializedModel);
        }
    }
}
```
***

To use this custom implementation, handle the **CreateCustomModelCacheManager** event in the _Program.cs_ file:

# [C#](#tab/tabid-csharp)

```csharp
winApplication.EnableModelCache = true;
winApplication.CreateCustomModelCacheManager += delegate(object sender, CreateCustomModelCacheManagerEventArgs e) {
    e.ModelCacheManager = new MyModelCacheManager();
};
winApplication.Setup();
winApplication.Start();
```
***

The Application Model cache is not used when the debugger is attached (see [Debugger.IsAttached](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.debugger.isattached#System_Diagnostics_Debugger_IsAttached)). So, the **CreateCustomModelCacheManager** is not triggered when you debug your application in Visual Studio. If you need to temporarily enable caching to debug your custom code, set the [ModelCacheManager.UseCacheWhenDebuggerIsAttached](xref:DevExpress.ExpressApp.ModelCacheManager.UseCacheWhenDebuggerIsAttached) field to **true** in the _WinApplication.cs_ file.

# [C#](#tab/tabid-csharp)

```csharp
ModelCacheManager.UseCacheWhenDebuggerIsAttached = true;
```
***

When you finished with debugging, remove this line. The model cache does not speed up your application startup in Visual Studio because the modules versions are constantly updated, and consequently, the cache is always recreated.
