// constants
const SET_USER = "session/SET_USER";
const REMOVE_USER = "session/REMOVE_USER";
const UNFOLLOW_USER = "session/UNFOLLOW_USER"
const FOLLOW_USER = "session/FOLLOW_USER"


const setUser = (user) => ({
	type: SET_USER,
	payload: user,
});

const removeUser = () => ({
	type: REMOVE_USER,
});

const removeFollowing = (user) => ({
	type: UNFOLLOW_USER,
	user
})

const newFollow = (user) => ({
	type: FOLLOW_USER,
	user
})



export const followUser = (username) => async (dispatch) => {
	const res = await fetch(`/api/users/follow/${username}`, {
		method: "POST"
	})
	if (res.ok) {
		dispatch(newFollow(username))
		let response = res.json()
		return response
	} else {
		let errors = res.json()
		return errors
	}
}

export const unfollowUser = (username) => async (dispatch) => {
	const res = await fetch(`/api/users/unfollow/${username}`,  {
		method: "DELETE"
	})
	// const res = await fetch(`/api/users/unfollow/${username}`)
	if (res.ok) {
		dispatch(removeFollowing(username))
		let response = res.json()
		return response
	} else {
		let errors = res.json()
		return errors
	}
}

export const authenticate = () => async (dispatch) => {
	const response = await fetch("/api/auth/", {
		headers: {
			"Content-Type": "application/json",
		},
	});
	if (response.ok) {
		const data = await response.json();
		if (data.errors) {
			return;
		}

		dispatch(setUser(data));
	}
};

export const login = (email, password) => async (dispatch) => {
	const response = await fetch("/api/auth/login", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({
			email,
			password,
		}),
	});
	
	if (response.ok) {
		const data = await response.json();
		dispatch(setUser(data));
		return null;
	} else if (response.status < 500) {
		const data = await response.json();
		if (data.errors) {
			return data.errors;
		}
	} else {
		return ["An error occurred. Please try again."];
	}
};

export const logout = () => async (dispatch) => {
	const response = await fetch("/api/auth/logout", {
		headers: {
			"Content-Type": "application/json",
		},
	});
	
	if (response.ok) {
		dispatch(removeUser());
	}
};

export const signUp = (username, email, password) => async (dispatch) => {
	const response = await fetch("/api/auth/signup", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({
			username,
			email,
			password,
		}),
	});
	
	if (response.ok) {
		const data = await response.json();
		dispatch(setUser(data));
		return null;
	} else if (response.status < 500) {
		const data = await response.json();
		if (data.errors) {
			return data.errors;
		}
	} else {
		return ["An error occurred. Please try again."];
	}
};

const initialState = { user: null, following: {}, followers: {} };

export default function reducer(state = initialState, action) {
	switch (action.type) {
		case FOLLOW_USER:
			let newState = {...state}
			let following = [...newState.user.following]
			following.push(action.user)
			newState.user.following = following
			console.log()
			return newState
		case SET_USER:
			return { user: action.payload };
		case REMOVE_USER:
			return { user: null };
		case UNFOLLOW_USER:
			let unfollowed = action.user
			let i = state.user.following.indexOf(unfollowed)
			console.log("state.user.following", state.user.following)
			console.log("state.user", state.user)
			state.user.following.slice(i, 1)
			return  {user: {...state.user}}
		default:
			return state;
	}
}