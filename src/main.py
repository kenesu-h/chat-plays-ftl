from model.iapplicationmodel import ApplicationModel
from model.applicationmodelimpl import ApplicationModelImpl
from viewmodel.iapplicationviewmodel import ApplicationViewModel
from viewmodel.applicationviewmodelimpl import ApplicationViewModelImpl
from view.iapplicationview import ApplicationView
from view.applicationviewimpl import ApplicationViewImpl

if __name__ == "__main__":
  model: ApplicationModel = ApplicationModelImpl()
  viewmodel: ApplicationViewModel = ApplicationViewModelImpl(model)
  view: ApplicationView = ApplicationViewImpl(viewmodel)
  view.initialize()
  # model.initialize()