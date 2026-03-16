---
uid: "112580"
title: How the XAF Application Model Works
owner: Andrey Kozhevnikov
---
# How the XAF Application Model Works

The **Application Model** is metadata that defines **the navigation structure, data presentation formats, and available commands**. XAF builds this metadata based on the application code. You can extend or customize the application model to add this functionality to your application. Users can also access the **Application Model** so that they can adjust their applications. 

The following image demonstrates the built-in **Model Editor** dialog. Try the **Edit Model** command in any of the **XAF** demos to access this editor.

![Application Model - End-User Editor](~/images/application-model-first-look.png)

## How XAF Uses the Application Model

When you run an XAF application, the framework performs the following steps:

1. Scans the application's code to generate the **Application Model**.
2. Populates the **Application Model** with default values. Learn about [node generators](xref:113316) and [model extenders](xref:403535) to understand how this process works and how you can control it. For extension examples, see [Extend and Customize the Application Model in Code](xref:112810).
3. Looks for previously saved model differences that change default values. (These could be user-made edits from previous application runs.) Applies these changes.
4. Creates UI elements based on up-to-date **Application Model** information.
5. You can change the **Application Model** after XAF creates the application's UI. In such cases, you need to force a UI refresh to reflect these changes. For a workaround, see the following article: [](xref:118592).

## What Code Takes Part in Application Model Generation

XAF calls the [](xref:DevExpress.ExpressApp.ModuleBase.GetExportedTypes)/[](xref:DevExpress.ExpressApp.ModuleBase.GetControllerTypes) methods for each [module](xref:118046) to discover classes that take part in the **Application Model** structure. These methods use [reflection](https://learn.microsoft.com/en-us/dotnet/framework/reflection-and-codedom/reflection) to locate the classes listed below.

 * **Business Object Model** <br/> These classes make up the **BOModel** node. For details on which classes make their way to this node, see [Add a Business Class](xref:112847) and [Non-Persistent Objects](xref:116516).
 * **Controller and Actions** <br/> These classes make up the **ActionDesign** node. For additional information, see [Controllers and Actions](xref:112621).


> [!NOTE]
> XAF uses only public classes to build the **Application Model**.


##  Application Model API

The **Application Model** is a tree of nodes. Each node type exposes its own property set.  

### Node Types / Interfaces

XAF defines an interface for each **Application Model** node type. All these interfaces share a common ancestor: [](xref:DevExpress.ExpressApp.Model.IModelNode). The members of this base interface allow property modification and access to the parent and child nodes.

One of the descendants is the  [](xref:DevExpress.ExpressApp.Model.IModelApplication) interface that corresponds to the root node (**Application**). This interface defines a few application-level properties (**Title**, **Company**, **Description**) and child nodes (**ActionDesign**, **Views**, and others). 

Review all available node interfaces: [Application Model - Built-in Interfaces](xref:403535).

### Node Extenders

XAF allows you to extend the Application Model - add properties or child nodes to existing nodes. The basic idea is that an "extender" interface (the one with additional properties or children) can attach to a node.  

You can use built-in extenders, such as [](xref:DevExpress.ExpressApp.SystemModule.IModelListViewFilters). This interface extends a **ListView** node with the **Filters** child. For the complete list of built-in extender interfaces, see [Application Model - Built-in Interfaces](xref:403535).

You can also extend **Application Model** nodes with custom properties and children. For samples, refer to the following article: [How to Extend the Application Model](xref:112810).

### Access and Modify the Application Model in Code

You can write code that obtains the Application Model object, accesses specific child nodes, and changes their settings. For samples, refer to the following article: [](xref:403527).   
  
## Application Model Layers 

On the one hand, XAF promotes code re-use and the same **Business Model** and **Controllers** can serve in multiple applications for different platforms. 

On the other hand, different applications may benefit from variations in UI layout. Different users can also tailor the applications to their own requirements.

This means that XAF must maintain the basic Application Model and variations that apply to the model on different levels:  

  -  **The zero layer** <br/> 
    XAF generates this layer based on the code of the application modules and referenced modules (as described earlier in this article).
  -  **Module-level differences** <br/>
    These platform-specific differences exist for each application module.  
  -  **Administrator differences** <br/> 
    These project-specific differences exist for each application project.
  -  **User differences** <br/> End-user customizations to the Application Model. These differences exist on each end-user machine.

If different layers have different values for the same property, XAF uses the value from a higher level. For example, a value from the 'User differences' layer has a higher priority than that of the 'Module-level' layer.


The following image illustrates this layered structure:

![Application Model: Differences on Multiple Levels](~/images/modelmergelayers.png)

## Application Model Differences: Storage Types

XAF can store Application Model changes (Model Differences) in different mediums. The `ModelStoreBase` class implements the basic storage functionality. The following descendants are available: 

- `FileModelStore` - XAFML file
- `ResourcesModelStore` - Project resource
- `ModelDifferenceDbStore` - Database
   
The default storage types for the layers are listed in the table below:

| Layer | Blazor | WinForms |
|---|---|---|
| Module-Level Differences | Assembly resources | Assembly resources |
| Administrator Differences | `FileModelStore` | `FileModelStore` |
| User Differences (No Security System) | (no storage)[^1] | `FileModelStore` |
| User Differences (With Security System) | `ModelDifferenceDbStore` | `ModelDifferenceDbStore` |

[^1]: To store changes for the **User Differences (No Security System)** layer in Blazor applications, handle the @DevExpress.ExpressApp.XafApplication.CreateCustomUserModelDifferenceStore event.

You can change storage type for Administrator and User differences. Subscribe to the following events: 

* Administrator differences: @DevExpress.ExpressApp.XafApplication.CreateCustomModelDifferenceStore
* User differences: @DevExpress.ExpressApp.XafApplication.CreateCustomUserModelDifferenceStore 

### File Storage Details

To store Model Differences in files, XAF uses *.xafml files that can be edited by the [Model Editor](xref:112582). There are two types of *.xafml files.

* **Model Differences** - contains general UI customizations
* **Model Difference Aspects** - contains localized UI customizations

![ModelDiffAspects](~/images/modeldiffaspects117612.png)
> [!TIP]
> To learn more about Application Model localization, refer to the following article: [Localization Basics](xref:112595).

The table below lists the names and locations of *.xafml files for different Application Model layers.

| Layer | Model Differences | Model Difference Aspects | Location |
|---|---|---|---|
| Module Level | _Model.DesignedDiffs.xafml_ | _Model.DesignedDiffs.Localization.\<[language code](https://learn.microsoft.com/en-us/dotnet/api/system.globalization.cultureinfo)>.xafml_ | Assembly resources |
| Administrator Level | _Model.xafml_ | _Model.\<[language code](https://learn.microsoft.com/en-us/dotnet/api/system.globalization.cultureinfo)>.xafml_ | Application folder |
| User Level | _Model.User.xafml_ | _Model.User.\<[language code](https://learn.microsoft.com/en-us/dotnet/api/system.globalization.cultureinfo)>.xafml_ | Application folder or the _%USERPROFILE%\AppData_ folder . |

The User Model Differences location is specified in the _App.config_ file. See the code below.

# [XML](#tab/tabid-xml)

```XML
<appSettings>
    <!-- ... -->
    <add key="UserModelDiffsLocation" value="CurrentUserApplicationDataFolder"/>
    <!-- ... -->
</appSettings>
```

***

Possible values are:

| Value | Description |
|---|---|
| **None** | User differences are not saved. |
| **ApplicationFolder** | Default value. User differences are stored in the application's working folder (together with the application executable). |
| **CurrentUserApplicationDataFolder** | User differences are stored in the user profile (the _%USERPROFILE%\AppData_ folder). |

### Database Storage Details
> [!TIP]
> If you need to enable **Database Storage** in an existing application, refer to the following help topic: [](xref:113698).

XAF uses two entities to store Model Differences in the database. The entities form a one-to-many relationship. 

![ModelDiffs_DB_Tables](~/images/modeldiffs_db_tables117613.png)

#### Model Difference

The [](xref:DevExpress.ExpressApp.IModelDifference) interface stores a collection of **Model Difference Aspects** for a user.

Each **Model Difference** has an associated user ([IModelDifference.UserId](xref:DevExpress.ExpressApp.IModelDifference.UserId)). An empty **UserId** means that the current Model Difference is shared by all users and is superimposed with their individual settings.

A Model Difference also defines an [IModelDifference.ContextId](xref:DevExpress.ExpressApp.IModelDifference.ContextId) that corresponds to the target platform. That way, separate sets of differences may be used for the same user when they run applications on a desktop or the web.

#### Model Difference Aspect

The [](xref:DevExpress.ExpressApp.IModelDifferenceAspect) interface stores a changed setting in the [IModelDifferenceAspect.Xml](xref:DevExpress.ExpressApp.IModelDifferenceAspect.Xml) property.

The [IModelDifferenceAspect.Name](xref:DevExpress.ExpressApp.IModelDifferenceAspect.Name) property sets the locale for the difference. If the property value is empty, the aspect applies to all languages.

> [!IMPORTANT]
> If you use the Integrated security mode or the Middle Tier server, ensure that all users have read/write access to **ModelDifference** and **ModelDifferenceAspect** types (users with read-only permissions cannot persist application customizations when exiting). **Read and write** permissions are required for the _Model.xafml_ file import operation. In the Middle Tier scenario, the **Create** permission is additionally required.

> [!NOTE]
> As an alternative for giving a user read-only permissions, you can use the [WinApplication.IgnoreUserModelDiffs](xref:DevExpress.ExpressApp.Win.WinApplication.IgnoreUserModelDiffs) property to ignore the **User's Model Differences**.
  
#### Shared Model Differences Management

The [Template Kit](xref:405447) generates, but comments out the code that enables database storage for shared model differences (administrator settings). That code is available in [!include[File_WinModule](~/templates/file_winmodule111231.md)] and [!include[File_WebModule](~/templates/file_webmodule111232.md)] files. 

XAF's default behavior is to always load design-time settings. 

You can uncomment the [XafApplication.CreateCustomModelDifferenceStore](xref:DevExpress.ExpressApp.XafApplication.CreateCustomModelDifferenceStore) event subscription. _Model.xafml_ file content will be loaded to the database once the application is started. XAF will ignore further changes to this file if the database record already exists for the shared model differences. To reload settings from _Model.xafml_, [enable the administrative UI](xref:113704) and use the **Import Shared Model Difference** Action (or delete the Shared Model Difference record and restart).

> [!NOTE]
> [!include[ThreadSafe_CustomFields_Note](~/templates/threadsafe_customfields_note111210.md)]
