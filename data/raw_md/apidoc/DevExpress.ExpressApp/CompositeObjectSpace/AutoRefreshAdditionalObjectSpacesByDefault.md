---
uid: DevExpress.ExpressApp.CompositeObjectSpace.AutoRefreshAdditionalObjectSpacesByDefault
name: AutoRefreshAdditionalObjectSpacesByDefault
type: Field
summary: Specifies whether Object Spaces refresh their inner Object Spaces from the @DevExpress.ExpressApp.CompositeObjectSpace.AdditionalObjectSpaces collection when refreshing themselves. This field affects all Object Spaces in your application if you do not specify the @DevExpress.ExpressApp.CompositeObjectSpace.AutoRefreshAdditionalObjectSpaces property for a particular Object Space.
syntax:
  content: public static bool AutoRefreshAdditionalObjectSpacesByDefault
  return:
    type: System.Boolean
    description: '**true**, if Object Spaces refresh their inner Object Spaces from the @DevExpress.ExpressApp.CompositeObjectSpace.AdditionalObjectSpaces collection when refreshing themselves; otherwise, **false**.'
seealso:
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/XAF_Non-Persistent-Objects-Reloading-Demo
  altText: How to refresh Non-Persistent Objects and reload nested Persistent Objects
---
If a non-persistent object contains a reference to or a collection of persistent objects, you need to refresh their Object Spaces after refreshing the parent non-persistent Object Space. Set this property to **true** to do this automatically each time the non-persistent Object Space refreshes.

After refreshing, drop all references and collections of outdated persistent objects and create new instances in refreshed persistent Object Spaces. Also, you can drop the non-persistent object with persistent objects it references and create a new instance again in the [ObjectsGetting](xref:DevExpress.ExpressApp.NonPersistentObjectSpace.ObjectsGetting), [ObjectGetting](xref:DevExpress.ExpressApp.NonPersistentObjectSpace.ObjectGetting), and [ObjectByKeyGetting](xref:DevExpress.ExpressApp.NonPersistentObjectSpace.ObjectByKeyGetting) event handlers.

The following example shows how to specify this static field for a WinForms application.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Win;
// ...
public partial class MySolutionWindowsFormsApplication : WinApplication {
    // ...
    public MySolutionWindowsFormsApplication() {
        NonPersistentObjectSpace.AutoRefreshAdditionalObjectSpacesByDefault = true;
        // ...
    }
}
```
***