---
uid: DevExpress.ExpressApp.CompositeObjectSpace.AutoDisposeAdditionalObjectSpacesByDefault
name: AutoDisposeAdditionalObjectSpacesByDefault
type: Field
summary: Specifies whether Object Spaces dispose of their inner Object Spaces from the @DevExpress.ExpressApp.CompositeObjectSpace.AdditionalObjectSpaces collection when they dispose of themselves. This field affects all Object Spaces in your application if you do not specify the @DevExpress.ExpressApp.CompositeObjectSpace.AutoDisposeAdditionalObjectSpaces property for a particular Object Space.
syntax:
  content: public static bool AutoDisposeAdditionalObjectSpacesByDefault
  return:
    type: System.Boolean
    description: '**true**, if Object Spaces dispose of their inner Object Spaces from the @DevExpress.ExpressApp.CompositeObjectSpace.AdditionalObjectSpaces collection when they dispose of themselves; otherwise, **false**.'
seealso:
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/XAF_Non-Persistent-Objects-Reloading-Demo
  altText: How to refresh Non-Persistent Objects and reload nested Persistent Objects
---
Dispose of Object Spaces that you stopped using because undisposed Object Spaces may lead to memory leaks. Set this property to **true** to automatically dispose of all additional Object Spaces simultaneously with the parent Object Space. 

The following example shows how to specify this static field for a WinForms application.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Win;
// ...
public partial class MySolutionWindowsFormsApplication : WinApplication {
    // ...
    public MySolutionWindowsFormsApplication() {
        CompositeObjectSpace.AutoDisposeAdditionalObjectSpacesByDefault = true;
        // ...
    }
}
```
***