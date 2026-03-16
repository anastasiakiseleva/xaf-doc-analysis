---
uid: DevExpress.ExpressApp.XafApplication.ListViewCreated
name: ListViewCreated
type: Event
summary: Occurs after a [List View](xref:112611) is created.
syntax:
  content: public event EventHandler<ListViewCreatedEventArgs> ListViewCreated
seealso: []
---
Handle this event to customize the [](xref:DevExpress.ExpressApp.ListView) that the [XafApplication.CreateListView](xref:DevExpress.ExpressApp.XafApplication.CreateListView*) method created. The **ListViewCreatedEventArgs.ListView** parameter specifies this List View.

The following example demonstrates how to handle this event in the _MySolution.Win\Program.cs_ file:

# [C#](#tab/tabid-csharp)

```csharp
using System;
using DevExpress.ExpressApp;
// ...
public class Program {
   public static void Main(string[] arguments) {
      MySolutionWinApplication winApplication = new MySolutionWinApplication();
      //...
      winApplication.ListViewCreated += winApplication_ListViewCreated;
   }
   private static void winApplication_ListViewCreated(object sender, ListViewCreatedEventArgs e) {
      if (e.ListView.Id == "Person_ListView"){
         e.ListView.CreateCustomCurrentObjectDetailView += 
            new EventHandler<CreateCustomCurrentObjectDetailViewEventArgs>(
            ListView_CreateCustomCurrentObjectDetailView);
      }
   }
   private static void ListView_CreateCustomCurrentObjectDetailView(object sender, 
         CreateCustomCurrentObjectDetailViewEventArgs e) {
      e.DetailViewId = "MyCustomDetailView";
   }
}
```
***
