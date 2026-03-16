---
uid: DevExpress.ExpressApp.Editors.ViewItem.SaveModel
name: SaveModel()
type: Method
summary: Saves the required information on the current state of the View Item to the [Application Model](xref:112580).
syntax:
  content: public void SaveModel()
seealso: []
---
This method is called by the [View.SaveModel](xref:DevExpress.ExpressApp.View.SaveModel) method for each View Item, to save their current state before setting a new value for the [View.Model](xref:DevExpress.ExpressApp.View.Model) property. After this property is changed, the View's settings are updated and the controls (View Items and their controls) are created (recreated, if they were previously created). So, you do not have to call this method manually.

This method calls the **SaveModelCore** method, which does nothing. However, you can override this method in the [](xref:DevExpress.ExpressApp.Editors.ViewItem) class' descendants, so that the required settings of your View Item's control are saved to the Application Model.