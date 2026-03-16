---
uid: DevExpress.ExpressApp.Xpo.XpoDataView.DefaultUseServerSideSorting
name: DefaultUseServerSideSorting
type: Property
summary: Indicates that the sort operation is executed on the server side before the result set is trimmed according to the `TopReturnedObjects` property. This property affects all List Views in your application if you do not specify the @DevExpress.ExpressApp.Xpo.XpoDataView.UseServerSideSorting property for a particular List View.
syntax:
  content: public static bool DefaultUseServerSideSorting { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true` if the sort operation is executed on the server side; `false` if the sort operation is executed on the client side. The default value is `true`.'
seealso: []
---
Specify the `DefaultUseServerSideSorting` property at startup before Views are created. For example, you can use constructors of the WinApplication (MySolution.Win\WinApplication.cs) and BlazorApplication (MySolution.Blazor.Server\BlazorApplication.cs) descendants.

### WinForms

**File**: _MySolution.Win\WinApplication.cs_.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Win;
using DevExpress.ExpressApp.Xpo;
// ...
public partial class MySolutionWindowsFormsApplication : WinApplication {
    // ...
    public MySolutionWindowsFormsApplication() {
        XpoDataView.DefaultUseServerSideSorting = false;
        // ...
    }
}
```
***

[!include[<DefaultUseServerSideSorting>](~/templates/solution_wizard_enables_property_in_new_projects.md)]

If you want to specify this option for a specific List View, use the @DevExpress.ExpressApp.Xpo.XpoDataView.UseServerSideSorting field instead.

> [!Note]
> With server-side sorting, you can use only persistent and aliased properties in the @DevExpress.ExpressApp.XafDataView.Sorting criteria. With client-side sorting, you can also use column names.
