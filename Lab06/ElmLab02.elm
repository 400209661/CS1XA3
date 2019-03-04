import Browser
import Html exposing (Html, Attribute, div, input, text)
import Html.Attributes exposing (..)
import Html.Events exposing (onInput)



-- MAIN


main =
  Browser.sandbox { init = init, update = update, view = view }



-- MODEL


type alias Model =
  { content : String
  , content2 : String
  }


init : Model
init =
  (Model "" "")



-- UPDATE


type Msg
  = Change String
  | Change2 String


update : Msg -> Model -> Model
update msg model =
  case msg of
    Change content ->
      { model | content = content }
    Change2 content2 ->
      { model | content2 = content2 }


-- VIEW


view : Model -> Html Msg
view model =
  div []
    [ input [ placeholder "String 1", value model.content, onInput Change ] []
    , input [ placeholder "String 2", value model.content2, onInput Change2 ] []
    , div [] [ text (model.content), text ":", text (model.content2) ]
    ]
