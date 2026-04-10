Use the [XafApplication.ResourcesExportedToModel](xref:DevExpress.ExpressApp.XafApplication.ResourcesExportedToModel) to access the collection of Resource Localizers.

**File:** _SolutionName.Win\Program.cs_

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Utils;
using DevExpress.ExpressApp.Win;
using DevExpress.Persistent.Base;
using DevExpress.XtraEditors;

namespace SolutionName.Win;

public class Program {
   public static void Main(string[] arguments) {
      SolutionNameWinApplication winApplication = new SolutionNameWinApplication();
      //...      
      winApplication.ResourcesExportedToModel.Add(typeof(
         <:0:>));
      winApplication.Setup();
      //...
   }
}
```