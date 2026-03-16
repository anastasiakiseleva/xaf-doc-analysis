---
uid: DevExpress.ExpressApp.XafApplication.BeginInit
name: BeginInit()
type: Method
summary: Starts the [](xref:DevExpress.ExpressApp.XafApplication)'s initialization. Initialization occurs at runtime.
syntax:
  content: public void BeginInit()
seealso: []
---
The Visual Studio .NET design-time environment calls this method to start initializing the application. The [XafApplication.EndInit](xref:DevExpress.ExpressApp.XafApplication.EndInit) method ends the initialization. Use the **BeginInit** and **EndInit** methods to prevent the application from being used until it has been completely initialized.