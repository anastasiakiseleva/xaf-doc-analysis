This example uses a Controller that sets different `ProtectedContentText` values for different List Views.

If the current List View displays objects of the `ProtectedContentRootObject` type, the `ProtectedContentText` property's value is changed to `"You cannot view inaccessible properties"`.

The following image illustrates the resulting List View's List Editor:

![ProtectedContentText](~/images/protectedcontenttext116110.png)


# [C#](#tab/tabid-csharp)

```csharp
using System;
using DevExpress.ExpressApp;

public partial class CustomProtectedStrings : ViewController {

   public CustomProtectedStrings() {           
      TargetViewType = ViewType.ListView;
      Activated += this.CustomProtectedStrings_Activated;
   }

   private void CustomProtectedStrings_Activated(object sender, EventArgs e) {
      if ((View as ListView).ObjectType == typeof(ProtectedContentRootObject)) {
         (View as ListView).Editor.ProtectedContentText = 
            "You cannot view inaccessible properties";
      }           
   }
}
```
***