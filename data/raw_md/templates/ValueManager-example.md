# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.Persistent.Base;

namespace MySolutionName.Module.Controllers {
    public class MyViewController : ViewController {
        protected override void OnActivated() {
            MyValue = "MyString"; // Store a value in ValueManager
            string myString = MyValue; // Get a value from ValueManager
        }
        public string MyValue {
            get {
                IValueManager<string> valueManager = ValueManager.GetValueManager<string>("myKey");
                if (valueManager.CanManageValue)
                    return valueManager.Value;
                else return "Some default value";
            }
            set {
                IValueManager<string> valueManager = ValueManager.GetValueManager<string>("myKey");
                if (valueManager.CanManageValue)
                    valueManager.Value = value;
            }
        }
    }
}
```
***
