---
uid: "114008"
seealso: []
title: "Hide the Protected Content Columns in a List View and Property Editors in a Detail View"
owner: Ekaterina Kiseleva
---
# Hide the Protected Content Columns in a List View and Property Editors in a Detail View

This topic describes how to use the [Conditional Appearance Module](xref:113286) in order to hide List View columns and Detail View Property Editors that are prohibited by the [Security System](xref:113366) and display the '\*\*\*\*\*\*\*' placeholders. 

* Add the Conditional Appearance Module to the platform-agnostic module project (if it was not added before). To do this, open the _MySolution.Module\Module.cs_ file and add the following code to the Module constructor:

	# [C#](#tab/tabid-csharp)

	```csharp
	using DevExpress.ExpressApp.ConditionalAppearance;
	// ...
	namespace MySolution.Module {
		public sealed partial class MySolutionModule : ModuleBase {
			public MySolutionModule() {
				// ...
				RequiredModuleTypes.Add(typeof(ConditionalAppearanceModule));
			}
		}
	}
	```

	***

* Implement the following [Controller](xref:112621) class in the platform-agnostic module project (_MySolution.Module_).
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	using DevExpress.ExpressApp;
	using DevExpress.ExpressApp.Editors;
	using DevExpress.ExpressApp.ConditionalAppearance;
	using DevExpress.ExpressApp.Security;
	// ...
	public class HideProtectedContentController : ViewController<ObjectView> {
	    private AppearanceController appearanceController;
	    protected override void OnActivated() {
	        base.OnActivated();
	        appearanceController = Frame.GetController<AppearanceController>();
	        if(appearanceController != null) {
	            appearanceController.CustomApplyAppearance += appearanceController_CustomApplyAppearance;
	        }
	    }
	    protected override void OnDeactivated() {
	        if(appearanceController != null) {
	            appearanceController.CustomApplyAppearance -= appearanceController_CustomApplyAppearance;
	        }
	        base.OnDeactivated();
	    }
	    void appearanceController_CustomApplyAppearance(object sender, ApplyAppearanceEventArgs e) {
	        if(e.AppearanceObject.Visibility == null || e.AppearanceObject.Visibility == ViewItemVisibility.Show) {
	            SecurityStrategy security = Application.GetSecurityStrategy();
				if(View is ListView) {
					if(e.Item is ColumnWrapper) {
						if (!security.CanRead(View.ObjectTypeInfo.Type, ObjectSpace,
                            ((ColumnWrapper)e.Item).PropertyName)) {
							e.AppearanceObject.Visibility = ViewItemVisibility.Hide;
						}
					}
				}
				if(View is DetailView) {
					if(e.Item is PropertyEditor) {
						object targetObject = e.ContextObjects.Length > 0 ? e.ContextObjects[0] : null;
                        if (targetObject != null) {
                            object key = View.ObjectSpace.GetKeyValue(targetObject);
                            bool canRead;
                            if (key != null) {
                                canRead = security.CanRead(View.ObjectTypeInfo.Type,
                                    View.ObjectSpace, key, ((PropertyEditor)e.Item).PropertyName);
                            }
                            else {
                                canRead = security.CanRead(View.ObjectTypeInfo.Type,
                                    View.ObjectSpace, ((PropertyEditor)e.Item).PropertyName);
                            }
                            if (!canRead) {
                                e.AppearanceObject.Visibility = ViewItemVisibility.Hide;
                            }
                        }
					}
				}
	        }
	    }
	}
	```

	***

> [!NOTE]
> * **HideProtectedContentController** may have a negative impact on the application performance in complex scenarios.
> * Hidden states of list view columns are persisted in user model differences. So, if you will eventually grant access to a certain property, the view model needs to be manually adjusted or reset.