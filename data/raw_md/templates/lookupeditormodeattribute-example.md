**File:** _SolutionName.Module/BusinessObjects/Employee.cs_

# [C#](#tab/tabid-csharp1)

```csharp
using DevExpress.Persistent.Base;

namespace SolutionName.Module.BusinessObjects;

public class Employee : BaseObject {
    // ...
    [LookupEditorMode(LookupEditorMode.AllItemsWithSearch)]
    public Department Department {
      // ...
    }
  }
```
***