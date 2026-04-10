---
uid: "113119"
seealso: []
title: Windows Forms Application Creation and Initialization
---
# Windows Forms Application Creation and Initialization

This topic details the steps performed after an end-user has run an XAF Windows Forms application, until the moment the main XAF objects, like the [](xref:DevExpress.ExpressApp.Win.WinApplication), are created and initialized.

In the following image, you can see that the entire process of application creation and initialization can be divided into four steps.

![WinApplicationInitialization](~/images/winapplicationinitialization116132.png)

&nbsp;

The table below describes all these steps in detail.

{|
|-

! Stage
! Description
! Ways to Interfere
|-

| Create an Application
| An instance of the **WinApplication** is created. This is performed by the **Program.Main** method, automatically generated in your Windows Forms application project.
| 
|-

| Initial Application Initialization
| A newly created application is initialized. The settings that are specified in the configuration file's _appSettings_ section are read to the application:
| 
|-

| 
| The location to be used to store the _Model.User.xafml_ file is specified by the **UserModelDiffsLocation** key.
| 
|-

| 
| The location to be used to store the application's Log file is specified by the **TraceLogLocation** key.
| 
|-

| 
| The [XafApplication.Modules](xref:DevExpress.ExpressApp.XafApplication.Modules) collection is populated by the modules added to the `Modules` collection. Each module is set up. The current `WinApplication` instance is assigned to the [ModuleBase.Application](xref:DevExpress.ExpressApp.ModuleBase.Application) property.
| If you need to add a module, use one of the following approaches:

Specify the required module name(s) in the application project's configuration file. Pass this string as a parameter of the [XafApplication.Setup](xref:DevExpress.ExpressApp.XafApplication.Setup*) method in the `Program.Main` method.

Add this module to the module that is contained in your solution. To do this, use the [ModuleBase.RequiredModuleTypes](xref:DevExpress.ExpressApp.ModuleBase.RequiredModuleTypes) collection.

To see code samples of both these approaches, refer to the [Ways to Register a Module](xref:118047) topic.

You can perform custom actions with a module, in addition to setting the Application object. To do this, override the module's [ModuleBase.Setup](xref:DevExpress.ExpressApp.ModuleBase.Setup*) method.
|-

| 
| The [XafApplication.Connection](xref:DevExpress.ExpressApp.XafApplication.Connection) property is set by applying one of the following techniques:

Specify the connection string in the application project's configuration file. Assign this string to the [XafApplication.ConnectionString](xref:DevExpress.ExpressApp.XafApplication.ConnectionString) property (see this property's description).

Set the [XafApplication.Connection](xref:DevExpress.ExpressApp.XafApplication.Connection) and/or [XafApplication.ConnectionString](xref:DevExpress.ExpressApp.XafApplication.ConnectionString) property before the [XafApplication.Setup](xref:DevExpress.ExpressApp.XafApplication.Setup*) method is called.
|-

| 
| The [XafApplication.Security](xref:DevExpress.ExpressApp.XafApplication.Security) property is set in the `Program.Main` method. The authentication strategy and the User type to be used by the [Security System](xref:113366) is specified in the same method.
| The **XAF** supplies the **SecurityStrategyComplex** security system type. If you need to use a custom security type that implements the **ISecurityStrategyBase** interface, create and assign it to the [XafApplication.Security](xref:DevExpress.ExpressApp.XafApplication.Security) property in code, before the [XafApplication.Setup](xref:DevExpress.ExpressApp.XafApplication.Setup*) method is called. If you need to use a custom authentication strategy or a custom User type, initialize them and the **XafApplication.Security** property, before the **XafApplication.Setup** method is invoked.

If you do not initialize a security system in code, a **SecurityDummy** will be used. This security type allows all operations with all types of objects. That is why the presence of the security system is invisible when you run an application.
|-

| 
| The [XafApplication.ApplicationName](xref:DevExpress.ExpressApp.XafApplication.ApplicationName) property is set to the value that is specified in the **Properties** grid when the **Application** section is selected.
| You can assign a custom value to the [XafApplication.ApplicationName](xref:DevExpress.ExpressApp.XafApplication.ApplicationName) property in code - before the [XafApplication.Setup](xref:DevExpress.ExpressApp.XafApplication.Setup*) method is called.
|-

| Application Initialization by the **Setup** method
| The [XafApplication.Setup](xref:DevExpress.ExpressApp.XafApplication.Setup*) method is called. This is performed by the **Program.Main** method that is automatically generated in your Windows Forms application project.

The **Setup** method has multiple overloads. XAF calls the method without parameters by default. It leaves the properties that are already initialized as they are, and proceeds with the initialization process using default values:
| You can call the **Setup** method with the required parameters, depending on what custom objects you need to create. However, we recommend that you use the approaches presented above, instead.
|-

| 
| A default splash screen form (DevExpress.ExpressApp.Win.Core.SplashScreen) is shown.
| You can set a custom splash screen using the [WinApplication.SplashScreen](xref:DevExpress.ExpressApp.Win.WinApplication.SplashScreen) property. The custom splash screen must implement the [](xref:DevExpress.ExpressApp.Win.ISplash) interface. To see an example, refer to the [](xref:400737) topic.
|-

| 
| A default Object Space Provider (see [XafApplication.ObjectSpaceProvider](xref:DevExpress.ExpressApp.XafApplication.ObjectSpaceProvider)) is created using the connection string specified by the [XafApplication.ConnectionString](xref:DevExpress.ExpressApp.XafApplication.ConnectionString) property.
| Refer to the following topic to learn how to create a custom Object Space Provider: <xref:405388>.
|-

| 
| A default Controllers Manager (**ControllersManager**) is created. This object contains a collection of all the Controllers that are declared in the registered modules.
| You can override the **XAFApplication.CreateControllersManager** method in your WinApplication class descendant. This method creates an instance of the built-in **ControllersManager** class. You can return an instance of another class.
|-

| 
| A default Modules Manager (**ApplicationModulesManager**) is created. This object contains the Modules collection with the modules to be used by the application. This collection is populated by the modules from the [XafApplication.Modules](xref:DevExpress.ExpressApp.XafApplication.Modules) collection. In addition, the **SystemModule** is added as a default module.
| You can override the **XAFApplication.GetDefaultModuleTypes** method in your WinApplication class descendant. This method creates an instance of the built-in **ApplicationModulesManager** class. You can return an instance of another class.

In addition, you can override the **GetDefaultModuleTypes** method to return modules to be added to the application by default, in addition to the System module.
|-

| 
| A default Application Model Differences Store (**FileModelStore**) is created.
| If you need to store an Application Model's differences in a place that is different from an XAFML file, you can create a custom Application Model Differences Store. To do this, subscribe to the [XafApplication.CreateCustomModelDifferenceStore](xref:DevExpress.ExpressApp.XafApplication.CreateCustomModelDifferenceStore) event before the **Setup** method is called, or override the **WinApplication.CreateModelDifferenceStoreCore** method in your WinApplication class descendant.
|-

| 
| The Object Space Provider and Controllers Manager are assigned to the application's corresponding properties: [XafApplication.ObjectSpaceProvider](xref:DevExpress.ExpressApp.XafApplication.ObjectSpaceProvider) and **ControllersManager**.
| Subscribe to the [XafApplication.SettingUp](xref:DevExpress.ExpressApp.XafApplication.SettingUp) event, to customize the objects to be assigned to the application object. Use the event handler's parameters to access the required objects.
|-

| 
| The Application Model Manager (**ApplicationModelsManager**) which manages the creation and initialization of the [Application Model](xref:112580) is instantiated.
| 
|-

| 
| The Application Model is created. Internally, the Application Model has a layered structure, so at first, the actual layers that comprise the Application Model internals are created:
| 
|-

| 
| The zero layer of the Application Model is created. Initially, it is empty. It is filled with data on demand, during the application life cycle.
| To extend the Application Model, pass the required model interfaces via the application modules' [ModuleBase.ExtendModelInterfaces](xref:DevExpress.ExpressApp.ModuleBase.ExtendModelInterfaces(DevExpress.ExpressApp.Model.ModelInterfaceExtenders)) methods. Alternatively, you can implement the [](xref:DevExpress.ExpressApp.IModelExtender) interface in [Controllers](xref:112621). To modify existing node generators, implement a generator updater and register it via the [ModuleBase.AddGeneratorUpdaters](xref:DevExpress.ExpressApp.ModuleBase.AddGeneratorUpdaters(DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters)) method of a module. For details, refer to the [Extend and Customize the Application Model in Code](xref:112810) topic.
|-

| 
| A layer for each module used in the application is created. This layer is filled with data from the _Model.DesignedDiffs.xafml_ file that contains Application Model differences created in a particular module.
| To modify this layer's data, modify the required module's XAFML file. This can be done, for example, via the [Model Editor](xref:112582).
|-

| 
| A layer for the application project is created. This layer is filled with data from the _Model.xafml_ file that contains Application Model differences created in the application project.
| To modify this layer's data, modify the application project's XAFML file. This can be done, for example, via the [Model Editor](xref:112582).
|-

| 
| Second, all the created layers are wrapped with the master layer.
| The master layer does not contain any information itself. It serves as a proxy for all other layers. Usually, when you access the Application Model, you deal with the master layer.
|-

| 
| The final state of the Application Model is assigned to the [XafApplication.Model](xref:DevExpress.ExpressApp.XafApplication.Model) property.
| Subscribe to the [XafApplication.SetupComplete](xref:DevExpress.ExpressApp.XafApplication.SetupComplete) event to create extra objects (helpers, extractors, etc.), after the application has been completely initialized.
|}
