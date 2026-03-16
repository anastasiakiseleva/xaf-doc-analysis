---
uid: DevExpress.ExpressApp.XafApplication.EnableModelCache
name: EnableModelCache
type: Property
summary: Specifies if the [Application Model](xref:112580) cache designed to improve the startup speed and performance is enabled.
syntax:
  content: |-
    [Browsable(false)]
    [DefaultValue(false)]
    public bool EnableModelCache { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true`, if the Application Model is cached; otherwise, `false`.'
seealso: []
---
If your WinForms application starts slowly, you can speed up the startup using the `EnableModelCache` property. When it is set to `true`, the Application Model content is cached to a file when the application is first launched, and recovered on subsequent runs. This property has effect in the production environment when the debugger is not attached (see [Debugger.IsAttached](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.debugger.isattached#System_Diagnostics_Debugger_IsAttached)). By default, `EnableModelCache` is set to `false`. To change this property value, add the following code to the _Program.cs_ file, before the [XafApplication.Setup](xref:DevExpress.ExpressApp.XafApplication.Setup*) method is called.

# [Program.cs](#tab/tabid-csharp)

```csharp
static void Main() {
    //..
    winApplication.EnableModelCache = true;
    winApplication.Setup();
    winApplication.Start();
}
```
***

As a result, [Nodes Generators and Generator Updaters](xref:112810) will be executed and the _Model.Cache.xafml_ cache file will be created only when the application is started for the first time. Note that the first startup can take more time than usual. However, the time taken by subsequent startups will be reduced, because the Application Model content will be recovered from the cache. The cache is recreated when the version of any application module is incremented.

The _Model.Cache.xafml_ file name is specified by the static [ModelStoreBase.ModelCacheDefaultName](xref:DevExpress.ExpressApp.ModelStoreBase.ModelCacheDefaultName) field.

When the cache is in use, consider the following.

* Only the `ModelNodeGenerator.UpdateCachedNodes` method is called for all Nodes Generators. If you need to create extra nodes after the Application Model is recovered from the cache file, override this protected method.
* Only the [ModelNodesGeneratorUpdater`1.UpdateCachedNode](xref:DevExpress.ExpressApp.Model.ModelNodesGeneratorUpdater`1.UpdateCachedNode(DevExpress.ExpressApp.Model.Core.ModelNode)) method is called for all Generator Updaters. If you need to update a certain node after it has been recovered from the cache file, override this method.

## Customize the Cache Location and Behavior
By default, the _Model.Cache.xafml_ file is located in the application folder. You can change its path using one of the following approaches.

* Override the `GetModelCacheFileLocationPath` method in [](xref:DevExpress.ExpressApp.XafApplication) descendant.
* Use the `ModelCacheLocation` key in the configuration file (_App.config_).
    
    # [XML](#tab/tabid-xml)
    
    ```XML
    <appSettings>
        <!-- ... -->
        <add key="ModelCacheLocation" value="CurrentUserApplicationDataFolder"/>
        <!-- ... -->
     </appSettings>
    ```
    
    ***

To customize the cache behavior, use static fields of the [](xref:DevExpress.ExpressApp.ModelCacheManager) class, or inherit this class and pass the descendant to the [XafApplication.CreateCustomModelCacheManager](xref:DevExpress.ExpressApp.XafApplication.CreateCustomModelCacheManager) event.

## When and Why is the Cache Updated?
To determine whether or not the cache file needs to be updated on startup, an XAF application compares the loaded modules versions with versions from the _ModulesVersionInfo_ file. This file stores versions for all modules which were used in the previous application launch. If there are no updated modules, the application loads the cache file; otherwise, the cache file is recreated. Modifying the cache options using the `ModelCacheManager` class does not enforce an immediate cache update. So, if you see that your customizations have no effect, ensure that at least one of your module versions is incremented, or delete the cache file manually.
