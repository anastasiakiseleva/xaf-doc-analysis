---
uid: DevExpress.ExpressApp.CollectionSourceBase.DisplayableProperties
name: DisplayableProperties
type: Property
summary: Provides access to the semicolon-delimited list of the [CollectionSourceBase.Collection](xref:DevExpress.ExpressApp.CollectionSourceBase.Collection)'s [Property Descriptors](xref:3113) and/or [expressions](xref:4928).
syntax:
  content: public string DisplayableProperties { get; set; }
  parameters: []
  return:
    type: System.String
    description: A semicolon-delimited list of the collection's property descriptors and/or expressions.
seealso: []
---
The example below illustrates how to set the **DisplayableProperties** property's value. Create a custom [Controller](xref:112621) and access the property from the **OnActivated** method and from the [ListView.CustomizeDisplayableProperties](xref:DevExpress.ExpressApp.ListView.CustomizeDisplayableProperties) event handler.

# [C#](#tab/tabid-csharp)

```csharp
using System;
using System.Collections.Generic;
using DevExpress.ExpressApp;
//...
public class MyViewController : ObjectViewController<ListView, Customer> {
    private List<string> additionalDisplayableProperties = 
        new List<string>() { "LocationContext.Flag", "LocationContext.Location.EntityNumberGenerationType" };
    protected override void OnActivated() {
        base.OnActivated();
            View.CollectionSource.DisplayableProperties = 
                GetUpdatedDisplayableProperties(View.CollectionSource.DisplayableProperties);
            View.CustomizeDisplayableProperties += View_CustomizeDisplayableProperties;
    }
    private void View_CustomizeDisplayableProperties(object sender, 
    CustomizeDisplayablePropertiesEventArgs e) {
        e.DisplayableProperties = GetUpdatedDisplayableProperties(e.DisplayableProperties);
    }
    private string GetUpdatedDisplayableProperties(string displayableProperties) {
        String result = displayableProperties;
        IList<String> displayablePropertiesList = displayableProperties.Replace("[", "").Replace("]", "").Split(';');
        foreach(string propertyName in additionalDisplayableProperties) {
            if(!displayablePropertiesList.Contains(propertyName)) {
                result = result + ";" + propertyName;
            }
        }
        return result;
    }
    protected override void OnDeactivated() {
        View.CustomizeDisplayableProperties -= View_CustomizeDisplayableProperties;
        base.OnDeactivated();
    }
}
```
***

> [!NOTE]
> [!include[DataView_PropertyName_Note](~/templates/dataview_propertyname_note111145.md)]