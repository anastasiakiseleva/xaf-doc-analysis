---
uid: DevExpress.ExpressApp.DetailView.#ctor(DevExpress.ExpressApp.IObjectSpace,System.Func{System.Threading.CancellationToken,System.Threading.Tasks.Task{System.Object}},DevExpress.ExpressApp.XafApplication,System.Boolean,System.Collections.IEnumerable)
name: DetailView(IObjectSpace, Func<CancellationToken, Task<Object>>, XafApplication, Boolean, IEnumerable)
type: Constructor
summary: Initializes a new instance of the @DevExpress.ExpressApp.DetailView class with specified settings.
syntax:
  content: public DetailView(IObjectSpace objectSpace, Func<CancellationToken, Task<object>> loader, XafApplication application, bool isRoot, IEnumerable objectsToPrefetch)
  parameters:
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object representing the Object Space that enables the created Detail View to work with a database.
  - id: loader
    type: System.Func{System.Threading.CancellationToken,System.Threading.Tasks.Task{System.Object}}
    description: ''
  - id: application
    type: DevExpress.ExpressApp.XafApplication
    description: An [](xref:DevExpress.ExpressApp.XafApplication) object that provides methods and properties to manage the current application.
  - id: isRoot
    type: System.Boolean
    description: '**true** to create a root Detail View; otherwise, **false**. This value is assigned to the [View.IsRoot](xref:DevExpress.ExpressApp.View.IsRoot) property.'
  - id: objectsToPrefetch
    type: System.Collections.IEnumerable
    description: ''
seealso: []
---
