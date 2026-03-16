---
uid: "113167"
title: 'How to: Display a List of Non-Persistent Objects with an Intermediate Container Class and Its Detail View'
---
# How to: Display a List of Non-Persistent Objects with an Intermediate Container Class and Its Detail View

This example stores a list of books. When a user clicks the **Show Duplicate Books** action, a pop-up dialog displays a list of duplicate books and their copy counts. This list is implemented as a [non-persistent object](xref:116516)'s Detail View.

![Book duplicates in a dialog popup](~/images/xaf-show-npo-in-popup.png)

This example uses an intermediate container class to display a list of non-persistent objects. In this case, the @DevExpress.ExpressApp.NonPersistentObjectSpace.ObjectsGetting method cannot be applied. If your application logic does not require complex operations to create non-persistent objects, use the @DevExpress.ExpressApp.NonPersistentObjectSpace.ObjectsGetting method. Refer to the following help topic for implementation details: <xref:114052>.

> [!Tip]
> You can find the complete example in the following GitHub repository: [How to: Display a List of Non-Persistent Objects with an Intermediate Container Class and Its Detail View](https://github.com/DevExpress-Examples/xaf-how-to-display-a-list-of-non-persistent-objects).

The following steps include the key implementation points:

## Step 1: Declare the `Book` Persistent Class
Objects of this class denote books in a collection.
    
# [Book.cs](#tab/tabid-cs-ef)
    
```csharp
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;

namespace NonPersistentListView.Module {
    [DefaultClassOptions]
    public class Book : BaseObject {
        public virtual string Title { get; set; }
    }
}
```
*** 

## Step 2: Declare Non-Persistent Classes

Declare two non-persistent classes—`Duplicate` and `DuplicatesList`, and decorate them with the @DevExpress.ExpressApp.DC.DomainComponentAttribute.

- The `Duplicate` class includes two properties—`Title` and `Count`. A class instance stores a unique book title and the total number of books with this title (if there is more than one book).
- The `DuplicatesList` class aggregates the `Duplicate` objects.

    
# [Duplicate.cs](#tab/tabid-cs)
    
```csharp
using System.ComponentModel;
using DevExpress.ExpressApp.DC;
using DevExpress.ExpressApp;

namespace NonPersistentListView.Module {
    [DomainComponent]
    public class Duplicate: NonPersistentLiteObject {
        public string Title { get; set; }
        public int Count { get; set; }
    }
    [DomainComponent]
    public class DuplicatesList: NonPersistentLiteObject {
        private BindingList<Duplicate> duplicates;
        public DuplicatesList() {
            duplicates = new BindingList<Duplicate>();
        }
        public BindingList<Duplicate> Duplicates { get { return duplicates; } }
    }
}
```
*** 

> [!NOTE]
> [!include[NonPersistent_RecommendedInterfaces](~/templates/nonpersistent_recommendedinterfaces111883.md)]

## Step 3: Register the Non-Persistent Object Space Provider
Ensure that the Non-Persistent Object Space Provider is registered in the Application Builder code. The [Template Kit](xref:405447) adds this code automatically.

# [Startup.cs](#tab/tabid-cs)

```csharp
// ...
builder.ObjectSpaceProviders
    // ...
    .AddNonPersistent();
// ...
```
*** 

## Step 4: Count the Number of Book Copies

Create the **ShowDuplicateBooksController** View Controller. In the controller, implement a method that iterates through persistent `Book` objects and counts the number of copies of each book. Store this information in a dictionary.

# [ShowDuplicateBooksController.cs](#tab/tabid-cs)

```csharp
// ...
private Dictionary<string, int> GetDuplicatesDictionary() {
    var dictionary = new Dictionary<string, int>();
    foreach(Book book in View.CollectionSource.List) {
        if(string.IsNullOrWhiteSpace(book.Title)) continue;
        dictionary[book.Title] = dictionary.GetValueOrDefault(book.Title) + 1;
    }
    return dictionary;
}
// ...
```
*** 

## Step 5: Create a List of Duplicate Objects

Implement a method that iterates through dictionary items and creates `Duplicate` objects for items with a value greater than one (books with more than one copy). Add `Duplicate` objects into a `DuplicatesList` collection.

# [ShowDuplicateBooksController.cs](#tab/tabid-cs)

```csharp
// ...
private DuplicatesList CreateDuplicatesList(Dictionary<string, int> duplicatesDictionary, IObjectSpace objectSpace) {
    DuplicatesList duplicatesList = objectSpace.CreateObject<DuplicatesList>();
    foreach(var (title, count) in duplicatesDictionary) {
        if(count <= 1) continue;

        var duplicate = objectSpace.CreateObject<Duplicate>();
        duplicate.Title = title;
        duplicate.Count = count;
        duplicatesList.Duplicates.Add(duplicate);
    }
    objectSpace.CommitChanges();
    return duplicatesList;
}
// ...
```
***

## Step 6: Add PopupWindowShowAction

Add the @DevExpress.ExpressApp.Actions.PopupWindowShowAction to display a popup dialog when a user clicks the **Show Duplicate Books** action. Handle the @DevExpress.ExpressApp.Actions.PopupWindowShowAction.CustomizePopupWindowParams event and call the @DevExpress.ExpressApp.XafApplication.CreateDetailView(DevExpress.ExpressApp.IObjectSpace,System.Object) method to create a Detail View for the `DuplicatesList` object.

# [ShowDuplicateBooksController.cs](#tab/tabid-cs)

```csharp
// ...
public ShowDuplicateBooksController() {
    PopupWindowShowAction showDuplicatesAction = new PopupWindowShowAction(this, "ShowDuplicateBooks", PredefinedCategory.View);
    showDuplicatesAction.CustomizePopupWindowParams += showDuplicatesAction_CustomizePopupWindowParams;
}
private void showDuplicatesAction_CustomizePopupWindowParams(object sender, CustomizePopupWindowParamsEventArgs e) {
    var duplicatesDictionary = GetDuplicatesDictionary();
    var nonPersistentObjectSpace = Application.CreateObjectSpace<DuplicatesList>();
    var duplicatesList = CreateDuplicatesList(duplicatesDictionary, nonPersistentObjectSpace);
    e.View = Application.CreateDetailView(nonPersistentObjectSpace, duplicatesList);
    e.DialogController.SaveOnAccept = false;
    e.DialogController.CancelAction.Active["NothingToCancel"] = false;
}
// ...
```
***

> [!spoiler][Show complete ShowDuplicateBooksController.cs code][Hide complete ShowDuplicateBooksController.cs code]
># [ShowDuplicateBooksController.cs](#tab/tabid-cs)
>
> ```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
using System.Collections;
>
>namespace NonPersistentListView.Module {
    public class ShowDuplicateBooksController : ObjectViewController<ListView, Book> {
        public ShowDuplicateBooksController() {
            PopupWindowShowAction showDuplicatesAction = new PopupWindowShowAction(this, "ShowDuplicateBooks", PredefinedCategory.View);
            showDuplicatesAction.CustomizePopupWindowParams += showDuplicatesAction_CustomizePopupWindowParams;
        }
        private void showDuplicatesAction_CustomizePopupWindowParams(object sender, CustomizePopupWindowParamsEventArgs e) {
            var duplicatesDictionary = GetDuplicatesDictionary();
            var nonPersistentObjectSpace = Application.CreateObjectSpace<DuplicatesList>();
            var duplicatesList = CreateDuplicatesList(duplicatesDictionary, nonPersistentObjectSpace);
            e.View = Application.CreateDetailView(nonPersistentObjectSpace, duplicatesList);
            e.DialogController.SaveOnAccept = false;
            e.DialogController.CancelAction.Active["NothingToCancel"] = false;
        }
        private Dictionary<string, int> GetDuplicatesDictionary() {
            var dictionary = new Dictionary<string, int>();
            foreach(Book book in View.CollectionSource.List) {
                if(string.IsNullOrWhiteSpace(book.Title)) continue;
                if(dictionary.TryGetValue(book.Title, out int count)) {
                    dictionary[book.Title] = count + 1;
                } else {
                    dictionary[book.Title] = 1;
                }
            }
            return dictionary;
        }
        private DuplicatesList CreateDuplicatesList(Dictionary<string, int> duplicatesDictionary, IObjectSpace objectSpace) {
            DuplicatesList duplicatesList = objectSpace.CreateObject<DuplicatesList>();
            foreach(var (title, count) in duplicatesDictionary) {
                if(count <= 1) continue;
                var duplicate = objectSpace.CreateObject<Duplicate>();
                duplicate.Title = title;
                duplicate.Count = count;
                duplicatesList.Duplicates.Add(duplicate);
            }
            objectSpace.CommitChanges();
            return duplicatesList;
        }
    }
}
> ```
> ***

## Result

The following images illustrate the implemented Action and its popup window.

### Windows Forms Application

![WinForms application: Non-persistent objects in a dialog popup](~/images/xaf-win-show-npo-in-popup.png)

### Blazor Application

![Blazor application: Non-persistent objects in a dialog popup](~/images/xaf-blazor-show-npo-in-popup.png)