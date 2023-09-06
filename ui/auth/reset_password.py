# # System # #

# # Packages # #
import streamlit as st

# # Project # #


###


class ResetError(Exception):
    """Raised when the reset password fails"""

    pass


class CredentialsError(Exception):
    """Raised when the reset password fails"""

    pass


class X:
    def __init__(self):
        self.username = None
        self.password = None

    def reset(self, username, form_name="Reset password"):
        reset_password_form = st.form("Reset password")

        reset_password_form.subheader(form_name)
        self.username = username.lower()
        self.password = reset_password_form.text_input(
            "Current password", type="password"
        )
        new_password = reset_password_form.text_input("New password", type="password")
        new_password_repeat = reset_password_form.text_input(
            "Repeat password", type="password"
        )

        if reset_password_form.form_submit_button("Reset"):
            if self._check_credentials(inplace=False):
                if len(new_password) > 0:
                    if new_password == new_password_repeat:
                        if self.password != new_password:
                            self._update_password(self.username, new_password)
                            return True
                        else:
                            raise ResetError("New and current passwords are the same")
                    else:
                        raise ResetError("Passwords do not match")
                else:
                    raise ResetError("No new password provided")
            else:
                raise CredentialsError

    def _check_credentials(self, inplace=True) -> bool:
        return True

    def _update_password(self, username, passwo) -> bool:
        return True


x = X()
x.reset("witt3rd")
